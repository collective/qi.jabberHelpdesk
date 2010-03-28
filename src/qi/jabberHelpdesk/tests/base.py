from Products.PloneTestCase import PloneTestCase
from Products.Five.testbrowser import Browser
from qi.jabberHelpdesk.tests.layer import JHelpdeskLayer
        
PloneTestCase.setupPloneSite()
        
class JHelpdeskTestCase(PloneTestCase.PloneTestCase):
    """We use this base class for all the tests in this package.
    """
    layer = JHelpdeskLayer

