import logging
from Products.CMFCore.utils import getToolByName

logger = logging.getLogger('qi.jabberHelpdesk')

def updateResourceRegistrations(context):
    
    kss_registry = getToolByName(context,'portal_kss')
    css_registry = getToolByName(context,'portal_css')
    
    logger.info('Unregistering old KSS resources')
    kss_registry.unregisterResource('++resource++qi.jabberHelpdesk.resources/helpdesk.kss')
    kss_registry.unregisterResource('++resource++qi.jabberHelpdesk.resources/helpdeskportlet.kss')
    
    logger.info('Re-registering KSS resources')
    registry = context.getImportStepRegistry()
    context.runImportStepFromProfile(profile_id='profile-qi.jabberHelpdesk:default',step_id='kssregistry')
    
    logger.info('Unregistering old CSS resources')
    css_registry.unregisterResource('++resource++qi.jabberHelpdesk.resources/helpdesk.css')
    logger.info('Re-registering CSS resources')
    context.runImportStepFromProfile(profile_id='profile-qi.jabberHelpdesk:default',step_id='cssregistry')
    
    logger.info('Updating icon resources')
    context.runImportStepFromProfile(profile_id='profile-qi.jabberHelpdesk:default',step_id='typeinfo')
    context.runImportStepFromProfile(profile_id='profile-qi.jabberHelpdesk:default',step_id='action-icons')
