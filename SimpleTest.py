import unittest
from appium import webdriver
from tools.data.global_data import *
from tools.HelperFunctions.custom_functions import *
from tools.desired_capabilities import ResetCapabilities
from tools.ex_conds import *


class LoginTests(unittest.TestCase, ResetCapabilities):
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_0_app_load(self):
        Action.element_visible(Action, SplashScreen.logo, 20)
        try:
            Action.element_has_text(Action, SplashScreen.login, 5, "Log in")
        except Exception as e:
            Action.element_has_text(Action, SplashScreen.login, 5, "LOG IN")
        finally:
            Action.element_click(Action, SplashScreen.continue_without_account, 5)

    def test_1_continue_page(self):
        Action.element_visible(Action, Dashboard.avatar, 10)













if __name__ == '__main__':
    unittest.main()
