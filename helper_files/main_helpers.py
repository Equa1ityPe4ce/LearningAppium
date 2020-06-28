import os
import unittest
from appium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from data_files.desired_capabilities import *
from ..data_files.global_data import *


def click_text(self, text):
    self.driver.find_element_by_xpath('//*[contains(@text, "{}")]'.format(text)).click()


def find_by_text(self, text):
    self.driver.implicitly_wait(1)
    if not self.driver.find_element_by_xpath('//*[contains(@text, "{}")]'.format(text)).is_displayed():
        print('Element is not displayed')
        return False
    else:
        print('Element is displayed')
        return True


def visible_assert(method, element):
    try:
        print(method, element)
        el = method, element
        print(el)
        if el:
            return True
        elif not el:
            return False
    except Exception:
        print('problem')
        return False


def search_cards(self):
    self.driver.implicitly_wait(5000)
    search_list = []
    row1xpath = ''
    row2xpath = ''
    xpathend = ''
    for index in range(1, 50):
        path1 = f"{row1xpath}{index}{xpathend}"
        path2 = f"{row2xpath}{index}{xpathend}"
        self.driver.implicitly_wait(1)
        if len(self.driver.find_elements(By.XPATH, path1)) > 0:
            self.driver.implicitly_wait(1)
            search_list.append(self.driver.find_element_by_xpath(f"{row1xpath}{index}{xpathend}").text)
            if len(self.driver.find_elements(By.XPATH, path2)) > 0:
                search_list.append(self.driver.find_element_by_xpath(f"{row2xpath}{index}{xpathend}").text)
        else:
            break
    return search_list


def search_any_text_in_list(text, results_in_list):
    if any(text in s for s in results_in_list):
        return True
    else:
        return False
