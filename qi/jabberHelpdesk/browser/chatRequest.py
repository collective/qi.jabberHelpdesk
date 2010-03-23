import logging
from zope.formlib import form
from zope.interface import implements
from zope.component import getMultiAdapter
from Products.CMFCore.utils import getToolByName


from Acquisition import aq_inner
from Products.Five.formlib import formbase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.statusmessages.interfaces import IStatusMessage

from plone.app.form import named_template_adapter
from plone.app.form.interfaces import IPlonePageForm
from zope.app.form.browser import TextAreaWidget
from qi.jabberHelpdesk.interfaces import IChatRequest
from qi.jabberHelpdesk import HelpdeskMessageFactory as _

logger = logging.getLogger('qi.jabberHelpdesk')
chatRequestFormView = named_template_adapter(ViewPageTemplateFile('chatRequest.pt'))
class SmallTextAreaWidget(TextAreaWidget):
    height = 5

class ChatRequestView(formbase.PageForm):
    """Request a chat
    """
    implements(IPlonePageForm)
    
    label = _(u"Chat with us")
    description = _(u"Welcome to our helpdesk")
    
    form_name =_(u"Please fill in your details")
    
    def __init__(self,context,request):
        ChatRequestView.label = context.title
        ChatRequestView.description = context.description
        self.mh = getMultiAdapter((context,request),name="helpdesk_xmlrpc")
        super(ChatRequestView,self).__init__(context,request)
    
    def availableAgents(self):
        try:
            botJid = self.context.botJid
            botPass = self.context.botPassword
            passHash = self.context.passwordHash()
            if self.mh.loadBot(botJid,botPass,self.context.persistent):
                return (len(self.mh.getAvailableAgents(botJid,passHash)),
                        len(self.mh.getAliveAgents(botJid,passHash)),)
            return (0,0)
        except:
            logger.error("Could not connect to bot:%s"%self.context.botJid)
            return (0,0)
    
    @property
    def form_fields(self):
        """ Note to self: I setup form_fields here as inside __init__ there is 
        no security context and I cannot get the authenticated member.
        I also set form_fields as a @property in order for it to be 
        instantiated after the form creation.
        """
        membership = getToolByName(self.context, 'portal_membership')
        self.memberName = None
        if not membership.isAnonymousUser():
            minfo = membership.getMemberInfo()
            self.memberName = unicode(minfo['fullname'] or
                str(membership.getAuthenticatedMember()))
        if self.memberName:
            ff = (form.FormFields(
                IChatRequest,for_display=True).select('name') +
                form.FormFields(IChatRequest).select('subject'))
            ff['name'].field.default=self.memberName
        else:
            ff = form.Fields(IChatRequest)
            ff['name'].field.default=u"Anonymous"
        ff['subject'].custom_widget  = SmallTextAreaWidget
        return ff
    
    @form.action(_(u"Submit"))
    def action_submit(self, action, data):
        """
        """
        
        context = aq_inner(self.context)
        subject = data['subject']
        if not data.has_key('name'):
            name = self.memberName
        else:
            name = data['name']
        
        try:
            if self.mh.loadBot(context.botJid,
                               context.botPassword,
                               context.persistent):
                if self.availableAgents()[0]:
                    return self.request.response.redirect(
                        '@@chatView?name=%s&subject=%s'%(name,subject))
                else:
                    IStatusMessage(self.request).addStatusMessage(
                        _(u"No available agents."), type='error')
            else:
                IStatusMessage(self.request).addStatusMessage(
                    _(u"Could not connect to helpdesk server"), type='error')
                logger.error(
                    "Could not connect to bot:%s"%self.context.botJid)
        
        except:
            IStatusMessage(self.request).addStatusMessage(
                _(u"Could not connect to helpdesk server"), type='error')
            logger.error("Could not connect to bot:%s"%self.context.botJid)
