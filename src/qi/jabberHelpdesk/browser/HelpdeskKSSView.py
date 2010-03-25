from zope.component import getMultiAdapter
import base64
from Acquisition import aq_inner

from plone.intelligenttext.transforms import convertHtmlToWebIntelligentPlainText, convertWebIntelligentPlainTextToHtml
from plone.app.kss.plonekssview import PloneKSSView
from random import choice
import string
from qi.jabberHelpdesk.browser.emoticons import replaceEmoticons
from qi.jabberHelpdesk import HelpdeskMessageFactory as _

msgFoot = '<dd class="msgFoot"><span class="msgBL"></span><span class="msgBR"></span></dd></dl>'
HtmlToText = convertHtmlToWebIntelligentPlainText
TextToHtml = convertWebIntelligentPlainTextToHtml

class HelpdeskKSSView(PloneKSSView):
    """
    """
    
    def __init__(self, *args):
        super(HelpdeskKSSView, self).__init__(*args)
        self.core = self.getCommandSet('core')
        self.plonekss = self.getCommandSet('plone')
        self.jhkss = self.getCommandSet('jabberHelpdesk')
        self.mh = getMultiAdapter((self.context,self.request),
                                  name="helpdesk_xmlrpc")
        self.botJid = self.context.botJid
        self.passHash = self.context.passwordHash()
    
    def login(self,userName,subject):
        """
        A user connects to the chat room.
        """
        # Generate unique userID
        chars = string.letters + string.digits
        userID = ''.join([choice(chars) for i in range(10)])
        self.core.setStateVar("helpdesk-userID",userID)
        self.core.setStateVar("helpdesk-lastMsgFrom",'')
        self.core.focus("#jabberHelpdeskMsgInput")
        try:
            
            agent=self.mh.userLogin(self.botJid,userID,userName,subject)
            vCard = self.mh.getAgentVCard(self.botJid,userID)
            self.core.setStateVar("helpdesk-lastMsgFrom",'')
            self.core.setStateVar("helpdesk-agent",agent)
            self.plonekss.issuePortalMessage(
                _(u"You are connected to the helpdesk. " \
                   "Someone will be with you shortly."),'info')
            vCardElem = self.core.getHtmlIdSelector("jabberHelpdeskAgentDetails")
            vCardDetails='<img id="agentAvatar" src="%s/helpdesk_avatar?userID=%s"/>'%(aq_inner(self.context).absolute_url(),userID)
            if vCard['FN'] or vCard['DESC']:
                vCardDetails += "<label>"+_(u"Talking with: ")+"</label>"+'<span id="jabberHelpdeskAgentDesc">'+vCard['FN']+" "+vCard['DESC']+"</span>"
            self.core.insertHTMLAsLastChild(vCardElem, vCardDetails)
        except Exception,Detail:
            return self._connectionError(Detail)
        return self.render()
    
    def logout(self,userID):
        """
        """
        self.mh.userLogout(self.botJid,userID)
        return self.render()
        
    
    def ping(self,userID,lastMsgFrom,userName='',message=None):
        """
        """
        try:
            (supportmessages,files) = self.mh.getUserMessages(self.botJid,userID)
        except Exception,Detail:
            return self._connectionError(Detail)
        
        if message:
            try:
                self.mh.sendUserMessage(self.botJid,userID,message)
                self.jhkss.jh_resetInput("#jabberHelpdeskMsgInput")
                self.core.focus("#jabberHelpdeskMsgInput")
            except Exception,Detail:
                return self._connectionError(Detail)
        
        self._updateMessages(supportmessages,message,lastMsgFrom,userName,userID,files)
        
        return self.render()
    
    def avatar(self,userID):
        b64 = self.mh.getAgentAvatarB64(self.botJid,userID)
        binary = base64.decodestring(b64)
        response = self.request.response
        response.setHeader('content-type', 'image/png')
        return binary
    
    def refreshAvailableAgents(self):
        
        aagents = self.mh.getAvailableAgents(self.botJid,self.passHash)
        oagents = self.mh.getAliveAgents(self.botJid,self.passHash)
        aaElem = self.core.getHtmlIdSelector("jabberHelpdeskAvailableAgents")
        oaElem = self.core.getHtmlIdSelector("jabberHelpdeskOnlineAgents")
        self.core.replaceInnerHTML(aaElem,str(len(aagents)))
        self.core.replaceInnerHTML(oaElem,str(len(oagents)))
        self.plonekss.issuePortalMessage(u"",'info')
        return self.render()
    
    def downloadChat(self,userID):
        discussion = self.mh.getDiscussion(self.botJid,userID)
        path = "/tmp/%s.txt"%userID
        from codecs import open
        output = open(path,"w","utf-8")
        output.write(discussion)
        output.close()
        b64 = base64.encodestring(path)
        href="%s/@@fileDownload?file=%s"%(self.context.absolute_url(),b64)
        self.core.replaceHTML("#jabberHelpdeskDownChat1",'<a id="jabberHelpdeskDownChat2" href="%s" target="_blank">Download chat transcript</a>'%href)
        return self.render()
    
    def _updateMessages(self,supportmessages,usermessage,
                        lastMsgFrom,userName,userID,files):
        """
        """
        
        messagesElem = self.core.getHtmlIdSelector("jabberHelpdeskMessages")
        lastMsg = self.core.getHtmlIdSelector("lastMsg")
        if supportmessages or files:
            msgElem = ''
            
            for message in supportmessages:
                message = message.encode('utf-8')
                message = convertHtmlToWebIntelligentPlainText(message)
                message = convertWebIntelligentPlainTextToHtml(message)
                message = message.replace("<a href",'<a target="_blank" href')
                message = replaceEmoticons(message)
                message = message.decode('utf-8')
                msgElem =msgElem+ '<dd><span>%s</span></dd>'%(message)
            for (path,name,descr) in files:
                b64 = base64.encodestring(path)
                href = "%s/@@fileDownload?file=%s"%(self.context.absolute_url(),b64)
                msgElem = msgElem + '<dd>You received a file:<a href=%s target="_blank">%s</a> %s</dd>'%(href,name,descr)
            
            if (lastMsgFrom!='support') and (not usermessage):
                msgHead = '<dl id="lastMsg" class="msgCont"><dt class="msgHead"><span class="msgTL"></span>'
                msgHead = msgHead+'<span class="tile">%s</span><span class="msgTR"></span></dt>'%('support')
                
                self.core.setAttribute(lastMsg,'id','')
                self.core.insertHTMLAsLastChild(messagesElem, msgHead+msgElem+msgFoot)
                self.core.setStateVar('helpdesk-lastMsgFrom','support')
                lastMsgFrom='support'
            else:
                self.core.replaceHTML("#lastMsg .msgFoot",msgElem+msgFoot)
            self.plonekss.issuePortalMessage('','info')
        
        if usermessage:
            usermessage = convertHtmlToWebIntelligentPlainText(usermessage)
            usermessage = convertWebIntelligentPlainTextToHtml(usermessage)
            usermessage = usermessage.replace("<a href",'<a target="_blank" href')
            usermessage = replaceEmoticons(usermessage)
            usermessage = usermessage.decode('utf-8')
            msgElem = '<dd><span>%s</span></dd>'%(usermessage)
            
            if lastMsgFrom !='user':
                msgHead = '<dl id="lastMsg" class="msgCont"><dt class="msgHead"><span class="msgTL"></span>'
                msgHead = msgHead +'<span class="tile">%s</span><span class="msgTR"></span></dt>'%(userName)
                self.core.setAttribute(lastMsg,'id','')
                self.core.insertHTMLAsLastChild(messagesElem, msgHead+msgElem+msgFoot)
                self.core.setStateVar('helpdesk-lastMsgFrom','user')
            else:
                self.core.replaceHTML("#lastMsg .msgFoot",msgElem+msgFoot)
        
        if supportmessages or usermessage or files:
            self.jhkss.jh_resetScrollbar(messagesElem)
    
    def _connectionError(self,Detail):
        """
        """
        self.plonekss.issuePortalMessage(_("Connection error"),'error')
        return self.render()
        