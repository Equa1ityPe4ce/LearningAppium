import os

from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
from selenium.webdriver.support.wait import *


# Activate Account Page
class ActivateAccount:
    check_box = (MobileBy.ACCESSIBILITY_ID, 'TermsCheckbox')
    continue_button = (MobileBy.ACCESSIBILITY_ID, 'ContinueButtonId')


# Login Page
class Login:
    email_field = (By.XPATH, '//android.view.View/android.view.View/android.widget.EditText[1]')
    password_field = (By.XPATH, '//android.widget.EditText[2]')
    sign_in = (By.XPATH, '//android.view.View[3]/android.widget.Button')


# Gate Selection
class GateSelection:
    jilia_hub = (By.XPATH, '(//android.widget.TextView[@content-desc="AddDevicesGatewayNameID"])[1]')
    qz3_hub = (By.XPATH, '(//android.widget.TextView[@content-desc="AddDevicesGatewayNameID"])[2]')
