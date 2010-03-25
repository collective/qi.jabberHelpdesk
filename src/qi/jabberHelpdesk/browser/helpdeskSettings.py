from zope.component import adapts
from zope.interface import implements
from zope.interface import Interface
from zope.formlib import form
from zope import schema

from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView

from plone.app.controlpanel.form import ControlPanelForm
from qi.jabberHelpdesk.interfaces import IHelpdeskSettings
from qi.jabberHelpdesk import HelpdeskMessageFactory as _

class HelpdeskSettings(BrowserView):
    
    implements(IHelpdeskSettings)
    
    def __init__(self, context, request):
        """ init view """
        self.context = context
        self.request = request
        portal_props = getToolByName(context, 'portal_properties')
        self.properties = getattr(portal_props, 'helpdesk_properties', None)
    
    def _get_property(self,property_id):
        if not self.properties:
            return None
        return getattr(self.properties,property_id)
    
    @property
    def xmlrpc_host(self):
        return self._get_property('xmlrpc_host')
    
    @property
    def xmlrpc_port(self):
        return int(self._get_property('xmlrpc_port'))


class IHelpdeskSettingsSchema(Interface):
    """
    Helpdesk xmlrpc server settings
    """
    
    xmlrpc_host = schema.TextLine(title=_(u"Helpdesk XMLRPC server"),
            description=_(u"The address of your local jabber xmlrpc server."),
            default=u'localhost',
            required=True)
    
    xmlrpc_port = schema.Int(title=_(u"Helpdesk XMLRPC server port "),
            description=_(u"The port of your XMLRPC server"),
            default=6666,
            required=True)


class HelpdeskControlPanel(ControlPanelForm):
    
    form_fields = form.FormFields(IHelpdeskSettingsSchema)
    
    label = _("Helpdesk settings")
    description = _("Server settings for the helpdesks of this site.")
    form_name = _("Helpdesk settings")

class HelpdeskControlPanelAdapter(SchemaAdapterBase):
    
    adapts(IPloneSiteRoot)
    implements(IHelpdeskSettingsSchema)
    
    def __init__(self, context):
        super(HelpdeskControlPanelAdapter, self).__init__(context)
        properties = getToolByName(context, 'portal_properties')
        self.context = properties.helpdesk_properties

    
    def get_xmlrpc_host(self):
        return getattr(self.context,'xmlrpc_host',"localhost")
    
    def set_xmlrpc_host(self, value):
        self.context._updateProperty('xmlrpc_host', value)
    
    xmlrpc_host = property(get_xmlrpc_host,set_xmlrpc_host)
    
    def get_xmlrpc_port(self):
        return int(getattr(self.context,'xmlrpc_port',"6667"))
    
    def set_xmlrpc_port(self, value):
        self.context._updateProperty('xmlrpc_port', value)
    
    xmlrpc_port = property(get_xmlrpc_port,set_xmlrpc_port)
