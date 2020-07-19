from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex_cond
from tools.desired_capabilities import ResetCapabilities


class Action(ResetCapabilities):

    def element_click(self, locator, timeout):
        element = WebDriverWait(self.driver, timeout).until(ex_cond.element_to_be_clickable(locator)).click()

    def element_invisible(self, locator, timeout):
        element = WebDriverWait(self.driver, timeout).until(ex_cond.invisibility_of_element_located(locator))

    def element_visible(self, locator, timeout):
        element = WebDriverWait(self.driver, timeout).until(ex_cond.visibility_of_element_located(locator))

    def get_text_from_element(self, locator, timeout):
        element = WebDriverWait(self.driver, timeout).until(ex_cond.presence_of_element_located(locator)).text

    def element_has_text(self, locator, timeout, text):
        element = WebDriverWait(self.driver, timeout).until(ex_cond.text_to_be_present_in_element(locator, text))
