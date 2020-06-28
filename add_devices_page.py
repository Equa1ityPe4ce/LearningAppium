import unittest
from appium import webdriver
from .Data.global_data import *
from .HelperFunctions.custom_functions import *


class AddDevices(unittest.TestCase):

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

    """
    --Precondition Set Up For The Test
    """
    def test_0_precondition(self):
        # Login
        self

        # navigate to add devices page
    """
    -Testing The Help Pop up on Add Devices Page
    """
    def test_1_help(self):
        # Select Help Button
        self
        # Observe correct Help message

        # close pop up

    """
    --Asserting The Hup Ip is displayed not "Not Available"
    """
    def test_2_hub_ip(self):
        # Assert Hub Ip is displayed not "Not Available"
        self


    """
    --Testing Add Hub Button
    """
    def test_3a_add_hub_button(self):
        # Button has text ADD HUB
        self

        # User can click button and is navigated to add Hub Page

    """
    --Testing Back Button
    """
    def test_3b_back_button(self):

        # Back button navigates user to add devices page
        self

    """
    -- Testing Not adding name or SGW and asserting
    """
    def test_4a_blank_form(self):
        # select activate button
        self
        # no pop up text

    """
    --Testing Adding a Blank SGW# and asserting the correct error message
    """
    def test_4b_blank_sgw(self):

        # Enter name for gateway
        self
        # select activate

        # pop up has appropriate error message that no SGW# was entered

    """
    --Testing the Formatting of the SGW for user.  Not requiring user to add SGW- or Case Sensitivity of field
    """
    def test_4c_CAPS_sgw_formatting(self):

        # Enter an SGW# with no SGW- and the input to be ALL CAPS eg. "ABCDEFG"
        self
        # select activatye button

        # if there is an offline pop up close it

        # assert the SGW# has been formatted to add the SGW- for user and the string is now lowercase

    """
    --Testing Attempting to activate a Hab that is off line and receiving the correct pop up
    """
    def test_4d_hub_offline(self):
        # clear SGW# field
        self
        # Enter in a SGW# with SGW-and lowercase using an offline hubs's SGW#

        # Assert Error Pop up stating "that hub is offline" in some fassion

    """
    -- Testing Trying to activate a Hub that is already assigned to the Account Pop up and error message
    """
    def test_4e_already_assigned(self):

        # Clear SGW#
        self
        # Enter an SGW# of a hub already activated to account (SGW-acdbda565dd3)

        # select activate

        # Assert Error Pop up stating "that hub is already on this account" in some fassion

    """
    -- Enable Pairing Help BUtton
    """
    def test_5_enable_help(self):
        # Select back button
        self
        # Select commissioned hub

        # Select help button

        # Observe Help text is appropriate

        # Close Help pop up

    """
    --Enable Pairing Button
    """
    def test_6a_enable_button(self):

        # Pairing button has text "ENABLE PAIRING"
        self
        # click that button

        # a text appears informing user how to pair shades to network

        # Buttons Text changes to CANCEL

    """
    -- Cancel PAiring
    """
    def test_6b_cancel_button(self):

        # Select CANCEL button
        self
        # Buttons Text Changes back to ENABLE PAIRING


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AddDevices)
    unittest.TextTestRunner(verbosity=2).run(suite)
