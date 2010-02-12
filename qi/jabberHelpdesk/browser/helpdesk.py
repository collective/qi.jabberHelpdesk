from zope.component import createObject
from zope.formlib import form

from plone.app.form import base

from Acquisition import aq_inner

from qi.jabberHelpdesk.interfaces import IHelpdesk
from qi.jabberHelpdesk import HelpdeskMessageFactory as _
        
        

class HelpdeskAddForm(base.AddForm):
    """Add form for jabber helpdesks
    """
    
    form_fields = form.Fields(IHelpdesk)
    
    label = _(u"Add jabber Helpdesk")
    form_name = _(u"Helpdesk settings")
    
    def create(self, data):
        helpdesk = createObject(u"qi.jabberHelpdesk.Helpdesk")
        form.applyChanges(helpdesk, self.form_fields, data)
        return helpdesk

class HelpdeskEditForm(base.EditForm):
    """Edit form for projects
    """
    
    form_fields = (form.Fields(IHelpdesk).select('title','description','persistent') +
                    form.Fields(IHelpdesk, for_display=True).select('botJid','botPassword'))
    
    label = _(u"Edit jabber Helpdesk")
    form_name = _(u"Helpdesk settings")