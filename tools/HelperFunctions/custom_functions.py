import os
import unittest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from ..data.global_data import *
from ..ex_conds import *
import random
import string



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


def visible_assert(self, element):
    self.driver.implicitly_wait(30)
    try:
        self.driver.find_element(element)
        print('Element is displayed')
        return True
    except NoSuchElementException as e:
        print('Element is not displayed')
        return False
    self.driver.implicitly_wait(20)

def standard_search(self,search_text, list_text):
    self.driver.implicitly_wait(20)
    Action.element_send_text(Action,Search.search_bar, 20, search_text)
    reddit_list = search_cards(self)
    print(reddit_list)
    self.assertTrue(search_any_text_in_list(list_text, reddit_list))

def search_cards(self):
    self.driver.implicitly_wait(5000)
    search_list = []
    row1xpath = '//android.widget.RelativeLayout['
    xpathend = ']/android.widget.TextView[1]'
    for index in range(1, 50):
        path1 = f"{row1xpath}{index}{xpathend}"
        self.driver.implicitly_wait(1)
        if len(self.driver.find_elements(By.XPATH, path1)) > 0:
            self.driver.implicitly_wait(1)
            search_list.append(self.driver.find_element_by_xpath(f"{row1xpath}{index}{xpathend}").text)
        else:
            break
    return search_list



def get_random_letters(self):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    random_string = []
    random_string = ''.join(random.choice(letters) for i in range(2))
    return random_string




def search_any_text_in_list(text, results_in_list):
    if any(text in s for s in results_in_list):
        return True
    else:
        return False
