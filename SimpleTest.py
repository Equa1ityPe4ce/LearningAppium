import unittest
import os
from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as ec, wait
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import *
from appium import webdriver
from .data_files.global_data import *
from time import sleep
from .data_files.desired_capabilities import des_cap
from .helper_files.main_helpers import *

"""
The main purpose of this Test is to give examples of
1. how to look for elements to be there
2. how to look for elements to not be there
3. calling selects from a page objects page
4. using methods
5. using the implicit_wait or what I like to call a sticky wait meaning 
   (once you set it, it stays that way until you change it)
"""
class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = des_cap(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    """
    Verifying user is on Activate Your Account Page and not the Login Page
    """
    def test_1_activate_Account_buttons_check(self):
        sleep(10)
        self.driver.implicitly_wait(2)
        self.assertTrue(visible_assert(self.driver.find_element, ActivateAccount.continue_button))
        self.assertTrue(visible_assert(self.driver.find_element, ActivateAccount.check_box))
        self.assertFalse(visible_assert(self.driver.find_element(*Login.sign_in)))

    """
    Clicking the required buttons to navigate to the login page
    """
    def test_2_activate_account_buttons_click(self):
        self.driver.find_element(*ActivateAccount.check_box).click()
        self.driver.find_element(*ActivateAccount.continue_button).click()
        self.driver.implicitly_wait(40)

    """
    Entering valid inputs for the email and password field. Also checking activate account page selector is not there
    """
    def test_3_login_page_valid(self):
        self.driver.find_element(*Login.email_field).is_displayed()
        self.driver.implicitly_wait(1)
        self.driver.find_element(*Login.email_field).send_keys("z.timgranger@gmail.com")
        self.driver.find_element(*Login.password_field).send_keys('Qwer1234')
        self.assertFalse(visible_assert(self.driver.find_element, ActivateAccount.continue_button))
        self.driver.find_element(*Login.sign_in).click()

    """
    Verifying user has made it to the Hub selection page and finishing the login process
    """
    def test_4_hub_selection(self):
        self.driver.find_element(*GateSelection.jilia_hub).is_displayed()
        self.driver.implicitly_wait(20)
        self.driver.find_element(*GateSelection.qz3_hub).click()


if __name__ == '__main__':
    unittest.main()
