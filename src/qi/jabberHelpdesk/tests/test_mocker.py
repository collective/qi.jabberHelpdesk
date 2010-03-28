from qi.jabberHelpdesk.tests.base import JHFunctionalTestCase

class TestMocker(JHFunctionalTestCase):
    """Test botfarm mocker object.
    """
    
    def test_userLogin(self):
        """Tests whether the botfarm mocker is available.
        """
        self.setRoles('Manager')
        self.folder.invokeFactory('Jabber Helpdesk','test')
        
        browser = self.getBrowser()
        browser.open(self.folder.test.absolute_url()+'/@@helpdesk_xmlrpc/userLogin?botID=bot&userID=user&name=smith&subject=letstalk')
        userLogin = browser.contents
        self.failUnless(userLogin=='agent@chatblox.com')

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestMocker))
    return suite
