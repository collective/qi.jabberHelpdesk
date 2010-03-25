import md5
from zope.interface import implements

from zope.component.factory import Factory
from plone.app.content.interfaces import INameFromTitle
from plone.app.content.item import Item
from qi.jabberHelpdesk.interfaces import IHelpdesk
from qi.jabberHelpdesk import HelpdeskMessageFactory as _

class Helpdesk(Item):
    implements(IHelpdesk, INameFromTitle)
    portal_type="Jabber Helpdesk"
    title=u""
    description = u""
    botJid = u""
    botPassword = u""
    persistent = False
    
    def __init__(self,id=None):
        super(Helpdesk,self).__init__(id)
    
    def passwordHash(self):
        """Returns a hash for the bot's password.
        """
        return md5.new(self.botPassword).hexdigest()

helpdeskFactory = Factory(Helpdesk, title=_(u"Create a new jabber helpdesk"))