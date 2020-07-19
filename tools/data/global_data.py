import os

from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy
from selenium import webdriver
from selenium.webdriver.support.wait import *

# Constant Globals

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
wait = 20
x_wait = 60


class SplashScreen:
    get_started = By.ID, "com.reddit.frontpage:id/signup_button"
    logo = By.ID, 'com.reddit.frontpage:id/launch_logo'
    login = By.ID, 'com.reddit.frontpage:id/login_button'
    continue_without_account = By.ID, 'com.reddit.frontpage:id/continue_without_account_button'

class Dashboard:
    avatar = MobileBy.ACCESSIBILITY_ID, 'Profile avatar'
