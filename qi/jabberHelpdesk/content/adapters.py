from qi.jabberHelpdesk.interfaces import IHelpdesk, IHelpdeskAgents
from zope.component import adapts
from zope.interface import implements
from zope.component import getMultiAdapter


class HelpdeskAgentsEditor(object):
    adapts(IHelpdesk)
    implements(IHelpdeskAgents)
    
    def __init__(self, context):
        self.context = context
        self.mh = getMultiAdapter((self.context,self.context.request),name="helpdesk_xmlrpc")
        self.mh.loadBot(self.context.botJid,self.context.botPassword,self.context.persistent)
    
    def _setAgents(self, value):
        oldAgents = self.mh.getHelpdeskAgents(self.context.botJid)
        toRemove = [agent for agent in oldAgents if agent not in value]
        toAdd = [agent for agent in value if agent not in oldAgents]
        for agent in toRemove:
            self.mh.removeAgent(self.context.botJid,agent)
        for agent in toAdd:
            self.mh.addAgent(self.context.botJid,agent)
    
    def _getAgents(self):
        return self.mh.getHelpdeskAgents(self.context.botJid)
    
    agentJids = property(_getAgents, _setAgents)