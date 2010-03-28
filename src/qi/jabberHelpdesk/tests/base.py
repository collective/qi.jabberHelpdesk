from Products.PloneTestCase import PloneTestCase
from Products.Five.testbrowser import Browser
from qi.jabberHelpdesk.tests.layer import JHelpdeskLayer
        
PloneTestCase.setupPloneSite()
        
class JHTestCase(PloneTestCase.PloneTestCase):
    """We use this base class for all the tests in this package.
    """
    layer = JHelpdeskLayer

class JHFunctionalTestCase(PloneTestCase.FunctionalTestCase):
    """We use this base class for all the tests in this package.
    """
    layer = JHelpdeskLayer

    def getCredentials(self):
        return '%s:%s' % (PloneTestCase.default_user,
            PloneTestCase.default_password)

    def getBrowser(self, loggedIn=True):
        """ instantiate and return a testbrowser for convenience """
        browser = Browser()
        if loggedIn:
            auth = 'Basic %s' % self.getCredentials()
            browser.addHeader('Authorization', auth)
        return browser
