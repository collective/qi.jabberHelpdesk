from zope.formlib import form
from plone.app.form import base
from qi.jabberHelpdesk.interfaces import IHelpdeskAgents
from qi.jabberHelpdesk import HelpdeskMessageFactory as _

class HelpdeskAgentsEditForm(base.EditForm):
    """Edit form for projects
    """
    
    form_fields = form.Fields(IHelpdeskAgents)
    
    label = _(u"Edit helpdesk agents")
    form_name = _(u"Helpdesk agents")