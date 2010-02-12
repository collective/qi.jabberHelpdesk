from zope.i18nmessageid import MessageFactory
from Products.CMFCore.permissions import setDefaultRoles

HelpdeskMessageFactory = MessageFactory('qi.jabberHelpdesk')
setDefaultRoles("qi.jabberHelpdesk: Add helpdesk", ('Manager',))
setDefaultRoles("qi.jabberHelpdesk: Use helpdesk", ('Anonymous',))

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
    pass
    