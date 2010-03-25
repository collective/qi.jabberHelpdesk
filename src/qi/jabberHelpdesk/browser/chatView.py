from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class ChatView(BrowserView):
    """
    """
    __call__ = ViewPageTemplateFile('chat.pt')
    
    def botJid(self):
        """
        """
        return self.context.botJid
    
    def render(self):
        """Simply return the template
        """
        return self.template()