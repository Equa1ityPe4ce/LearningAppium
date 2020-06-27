import os

from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy
from selenium import webdriver
from selenium.webdriver.support.wait import *

# Constant Globals

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
wait = WebDriverWait(webdriver, 20)
x_wait = WebDriverWait(webdriver, 20)


class ActivateAccount(object):
    CHECK_BOX = (MobileBy.ACCESSIBILITY_ID, 'TermsCheckbox')
    CONTINUE_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'ContinueButtonId')
    # check_box = 'TermsCheckBox'
    # cont_btn = str('ContinueButtonID')


# Login Page
class Login:
    EMAIL_FIELD = (By.XPATH, '//android.view.View/android.view.View/android.widget.EditText[1]')
    PASSWORD_FIELD = (By.XPATH, '//android.widget.EditText[2]')
    SIGN_IN = (By.XPATH, '//android.view.View[3]/android.widget.Button')


# Gate Selection
class GateSelection:
    JILIA_HUB = (By.XPATH, '(//android.widget.TextView[@content-desc="AddDevicesGatewayNameID"])[1]')
    QZ3_HUB = (By.XPATH, '(//android.widget.TextView[@content-desc="AddDevicesGatewayNameID"])[2]')
