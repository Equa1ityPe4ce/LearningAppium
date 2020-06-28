import os
from appium import webdriver


def des_cap(self):
    PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )
    desired_caps = {
        "automationName": "UiAutomator2",
        "platformName": "Android",
        "deviceName": 'Android',
        "App": PATH('..\\App\\com.legrand.QMotionJiliaApp.apk'),
        "appPackage": "com.legrand.QMotionJiliaApp",
        "appActivity": "qmotion.splashactivity",
        "autoGrantPermissions": "true"
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(60)

    return driver


def no_reset_caps(self):
    PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )
    desired_caps = {
        "automationName": "UiAutomator2",
        "platformName": "Android",
        "deviceName": 'Android',
        "App": PATH('..\\App\\com.legrand.QMotionJiliaApp.apk'),
        "appPackage": "com.legrand.QMotionJiliaApp",
        "appActivity": "qmotion.splashactivity",
        "autoGrantPermissions": "true",
        "noReset": "true"
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(60)

    return driver
