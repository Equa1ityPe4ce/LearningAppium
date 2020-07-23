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

class Search:
    search_bar = By.ID, 'com.reddit.frontpage:id/search'
    search_bar_view = By.ID, 'com.reddit.frontpage:id/search_view'
    click_card1 = By.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]'
    Back_home = By.XPATH, '//android.widget.FrameLayout[1]/android.widget.ImageView'
    description = By.ID, 'com.reddit.frontpage:id/profile_description'
    dog_search = By.ID, 'com.reddit.frontpage:id/profile_title'


class post_type:

    post_choice = By.ID, 'com.reddit.frontpage:id/sort_description'
    post_hot = By.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]'
    post_new = By.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]'
    vote = By.ID, 'com.reddit.frontpage:id/vote_view_score'
    post_top = By.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]'
    post_controversial = By.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[4]'
    post_rising = By.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[5]'
    past_hour = By.XPATH,'//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView'
    past_24 = By.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView'
    past_week = By.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.TextView'
    past_month = By.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[4]/android.widget.TextView'
    past_year = By.XPATH,'//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[5]/android.widget.TextView'
    all_time = By.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[6]/android.widget.TextView'

class location:
    location_selector = By.ID, 'com.reddit.frontpage:id/geopopular_selection_text'
    my_location_selector = By.XPATH, '//android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.CheckedTextView'
    other_location = By.XPATH, '//android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.CheckedTextView'
    CROATIA = By.XPATH, '//android.view.ViewGroup[8]/android.widget.TextView[1]'
    global_selector = By.XPATH, '//android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.CheckedTextView'

class card_view:
    view_selector = By.ID, 'com.reddit.frontpage:id/view_mode'
    classic_selector = By.XPATH, '//android.widget.LinearLayout[2]/android.view.ViewGroup/android.widget.TextView'
    card_selector =  By.XPATH, '//android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.TextView'

class coins:
    get_coins = MobileBy.ACCESSIBILITY_ID, 'Get Coins'
    coin_header = By.ID, 'com.reddit.frontpage:id/buy_coins_toolbar_image'
    buy_coins = By.ID, 'com.reddit.frontpage:id/buy_coin_best_buybutton'
    coins_back = By.XPATH, '//android.widget.LinearLayout/android.view.ViewGroup/android.widget.ImageButton'

class navigate:
    home = By.XPATH, '//i3.b.a.a.c[@content-desc="Home"]/android.widget.TextView'
    popular = By.XPATH,'//i3.b.a.a.c[@content-desc="Popular"]/android.widget.TextView'

