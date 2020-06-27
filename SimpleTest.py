from appium import webdriver
from .Data.global_data import *
from .HelperFunctions.custom_functions import *


class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        desired_caps = {
            "automationName": "UiAutomator2",
            "platformName": "Android",
            "deviceName": 'Android',
            "App": PATH('..\\App\\com.legrand.QMotionJiliaApp.apk'),
            "appPackage": "com.legrand.QMotionJiliaApp",
            "appActivity": "qmotion.splashactivity",
            "autoGrantPermissions": "true"
        }
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_1_nav_to_login(self):
        self.driver.implicitly_wait(20)
        self.assertTrue(self.driver.find_element(*ActivateAccount.CONTINUE_BUTTON).is_displayed())
        self.assertTrue(EC.element_to_be_clickable(ActivateAccount.CHECK_BOX))
        self.driver.find_element(*ActivateAccount.CHECK_BOX).click()
        self.driver.find_element(*ActivateAccount.CONTINUE_BUTTON).click()

    def test_2_login(self):
        self.driver.find_element(*Login.EMAIL_FIELD).is_displayed()
        self.assertFalse(visible_assert(self, ActivateAccount.CONTINUE_BUTTON))


if __name__ == '__main__':
    unittest.main()
