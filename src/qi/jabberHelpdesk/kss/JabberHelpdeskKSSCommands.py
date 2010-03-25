from qi.jabberHelpdesk.kss.IJabberHelpdeskKSSCommands import IJabberHelpdeskKSSCommands
from kss.core import CommandSet
from zope import interface

class JabberHelpdeskKSSCommands(CommandSet):
    interface.implements(IJabberHelpdeskKSSCommands)
    
    def jh_resetScrollbar(self, selector):
        command = self.commands.addCommand('jh_resetScrollbar', selector)
    def jh_resetInput(self, selector):
        command = self.commands.addCommand('jh_resetInput', selector)
