import unittest
from appium import webdriver
from tools.data.global_data import *
from tools.HelperFunctions.custom_functions import *
from tools.desired_capabilities import ResetCapabilities
from tools.ex_conds import *
import random
import string
import time

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

    def test_1b_search_page(self):
        Action.element_visible(Action, Search.search_bar_view, 10)
    def test_2_search_page(self):
        Action.element_click(Action, Search.search_bar_view, 10)
    def test_3_search_page(self):
        search = self.driver.find_element_by_id('com.reddit.frontpage:id/search_view')
        search.click()
    def test_3a_search_page(self):
       for i in range(1):
            self.driver.implicitly_wait(10)
            from_cf_random_letters = get_random_letters(self)
            standard_search(self,from_cf_random_letters, from_cf_random_letters)
            Action.element_click(Action, Search.click_card1, 10)
            sub_description = self.driver.find_element_by_id('com.reddit.frontpage:id/profile_description')
            text = sub_description.text
            print(text)
            self.driver.implicitly_wait(20)
            Action.element_click(Action, Search.Back_home, 10)

    def test_3b_search_by_word(self):
        Action.element_click(Action, Search.search_bar_view, 10)
        Action.element_send_text(Action, Search.search_bar, 10, 'dogs')
        Action.element_click(Action, Search.click_card1, 10)
        Action.element_click(Action, Search.Back_home, 10)
        #TODO figure out why this didn't work.

    def test_4_post_types(self):
        self.driver.implicitly_wait(10)
        Action.element_click(Action,post_type.post_choice,10)
        Action.element_click(Action,post_type.post_new, 10)
        self.driver.implicitly_wait(10)
        # testing if new is actually new
        new_vote_text = self.driver.find_element_by_xpath('//android.widget.LinearLayout[1]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView')
        first_test_vote_text = new_vote_text.text
        self.assertEqual(first_test_vote_text, "Vote")

    def test_4a_post_types(self):
        Action.element_click(Action, post_type.post_choice, 10)
        Action.element_click(Action, post_type.post_top, 10)
        Action.element_click(Action, post_type.past_month, 10)
        Action.element_click(Action, post_type.post_choice, 10)
        Action.element_click(Action, post_type.post_controversial, 10)
        Action.element_click(Action, post_type.past_hour, 10)
        Action.element_click(Action, post_type.post_choice, 10)
        Action.element_click(Action, post_type.post_rising, 10)
        Action.element_click(Action, post_type.post_choice,10)
        Action.element_click(Action, post_type.post_hot, 10)

    def test_5_locations(self):
        Action.element_click(Action, location.location_selector, 10)
        Action.element_click(Action, location.my_location_selector, 10)
        time.sleep(10)
        location_text_test = self.driver.find_element_by_id('com.reddit.frontpage:id/geopopular_selection_text')
        test_location = location_text_test.text
        self.assertEqual(test_location, "UNITED STATES")

    def test_5a_locations(self):
        Action.element_click(Action, location.location_selector, 10)
        Action.element_click(Action, location.other_location, 10)
        Action.element_click(Action, location.CROATIA, 10)
        time.sleep(5)
        # Action.element_has_text(Action, location.CROATIA, 10, "CROATIA")
        Action.element_click(Action, location.location_selector,10)
        Action.element_click(Action, location.global_selector, 10)
        # CROATIA_test = self.driver.find_element_by_xpath('//android.view.ViewGroup[8]/android.widget.TextView[1]')
        # CROATIA_test_final= CROATIA_test.text
        # self.assertEqual(CROATIA_test_final, "CROATIA")
        #TODO: figure out why this didn't work

    def test_6_cardview(self):
        Action.element_click(Action, card_view.view_selector, 10)
        Action.element_click(Action, card_view.classic_selector,10)
        Action.element_click(Action, card_view.view_selector, 10)
        Action.element_click(Action, card_view.card_selector, 10)

    def test_7_coins(self):
        Action.element_click(Action, coins.get_coins, 10)
        Action.element_has_text(Action, coins.buy_coins, 5, "$5.99")
        Action.element_click(Action, coins.coins_back, 10)

    def test_8_nav_button(self):
        Action.element_click(Action, navigate.home, 10)
        Action.element_click(Action, navigate.popular, 10)

if __name__ == '__main__':
    unittest.main()
