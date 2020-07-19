import os
from appium import webdriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class ResetCapabilities:
    desired_caps = {
        'platformName': 'Android',
        'automationName': 'UiAutomator2',
        'deviceName': 'Android',
        'app': PATH('..\\tools\\app\\com.reddit.frontpage.apk'),
        "appPackage": "com.reddit.frontpage",
        "appActivity": ".StartActivity",
        "ignoreUnimportantViews": "true",
        "autoGrantPermissions": "true",

    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(20)
