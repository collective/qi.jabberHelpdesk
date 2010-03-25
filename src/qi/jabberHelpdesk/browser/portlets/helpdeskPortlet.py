import logging
from zope import schema
from zope.component import getMultiAdapter
from zope.formlib import form
from zope.interface import implements

from plone.app.portlets.portlets import base
from plone.app.vocabularies.catalog import SearchableTextSourceBinder
from plone.app.form.widgets.uberselectionwidget import UberSelectionWidget
from plone.portlets.interfaces import IPortletDataProvider

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from qi.jabberHelpdesk import HelpdeskMessageFactory as _
from qi.jabberHelpdesk.interfaces import IHelpdesk


logger = logging.getLogger('qi.jabberHelpdesk')

class IHelpdeskPortlet(IPortletDataProvider):
    """
    """
    targetHelpdesk = schema.Choice(title=_(u"Target helpdesk"),
            description=_(u"Link to the helpdesk of your choice"),
            required=True,
            source=SearchableTextSourceBinder({'object_provides' : IHelpdesk.__identifier__},default_query='path:')
    )
    
    portletImage = schema.Choice(title=_(u"Portlet image"),
            description=_(u"An image to be displayed in the body of the portlet"),
            required=True,
            source=SearchableTextSourceBinder({'portal_type' : 'Image' },default_query='path:')
    )


class Assignment(base.Assignment):
    """
    """
    
    implements(IHelpdeskPortlet)
    def __init__(self,targetHelpdesk=[],portletImage=[]):
        self.targetHelpdesk = targetHelpdesk
        self.portletImage = portletImage
    
    @property
    def title(self):
        return _(u"Helpdesk portlet")

class Renderer(base.Renderer):
    
    render = ViewPageTemplateFile('helpdeskPortlet.pt')
    
    def __init__(self, context, request, view, manager, data):
        """
        """
        self.context = context
        self.request = request
        self.data = data
        self.helpdesk = self._getFromPath(self.data.targetHelpdesk)
        self.image = self._getFromPath(self.data.portletImage)
        self.mh = getMultiAdapter((self.context,self.request),name="helpdesk_xmlrpc")
        pm = getToolByName(self.context,'portal_membership')
        member = pm.getAuthenticatedMember()
        self.permissionGrant =  member.has_permission('qi.jabberHelpdesk: Use helpdesk',self.context)
    
    @property
    def availableAgents(self):
        """
        """
        try:
            if self.mh.loadBot(self.helpdesk.botJid,
                               self.helpdesk.botPassword,
                               self.helpdesk.persistent):
                available = self.mh.getAvailableAgents(
                    self.helpdesk.botJid,
                    self.helpdesk.passwordHash()) 
                return len(available)
            return 0
        except:
            return 0
    
    
    @property
    def available(self):
        """
        """
        return self.permissionGrant and self.availableAgents
    
    @property
    def helpdeskLink(self):
        """
        """
        return self.helpdesk.absolute_url()
    
    @property
    def helpdeskImage(self):
        """
        """
        return self.image.absolute_url()
    
    def _getFromPath(self,path):
        """ gets the object the path is pointing to"""
        if path.startswith('/'):
            path = path[1:]
        if not path:
            return None
        portal_state = getMultiAdapter((self.context, self.request), name=u'plone_portal_state')
        portal = portal_state.portal()
        return portal.unrestrictedTraverse(path, default=None)

class AddForm(base.AddForm):
    form_fields = form.Fields(IHelpdeskPortlet)
    form_fields['targetHelpdesk'].custom_widget = UberSelectionWidget
    form_fields['portletImage'].custom_widget = UberSelectionWidget
    
    label = _(u"Add helpdesk portlet")
    description = _(u"This portlet lets people ask for online support from the helpdesk.")
    
    def create(self,data):
        return Assignment(**data)
        #return Assignment(targetHelpdesk=data.get('targetHelpdesk',[]),
        #               portletImage=data.get('portletImage',[]))

class EditForm(base.EditForm):
    form_fields = form.Fields(IHelpdeskPortlet)
    form_fields['targetHelpdesk'].custom_widget = UberSelectionWidget
    form_fields['portletImage'].custom_widget = UberSelectionWidget
    label = _(u"Edit helpdesk portlet")
    description = _(u"This portlet lets people ask for online support from the helpdesk.")
