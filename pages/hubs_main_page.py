from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from test_data.test_data import HUBS_MAIN_URL, SIGN_UP_URL, QUOTE_URL
from utilities.utils import Utils


class HubsMainPage:
    PROFILE_BTN = "h3d-navbar__user"
    REGISTER_BTN = "//*[@id='h3d-navbar__user']/div/div/a[2]"
    GET_QUOTE_BTN = "#content > div > div.cnc-hero.cnc-hero--with-image > div > div.content > div.wrap.wrap--with-logos > div > div > a"

    def __init__(self, driver):
        self.driver = driver

    def register(self):
        ut = Utils(self.driver)
        WebDriverWait(self.driver, 60).until(ec.url_to_be(HUBS_MAIN_URL))
        ut.click_by_id(self.PROFILE_BTN)
        ut.click_by_xpath(self.REGISTER_BTN)
        WebDriverWait(self.driver, 60).until(ec.url_to_be(SIGN_UP_URL))

    def create_instant_quote(self):
        ut = Utils(self.driver)
        WebDriverWait(self.driver, 60).until(ec.url_to_be(HUBS_MAIN_URL))
        ut.click_by_css_js(self.GET_QUOTE_BTN)
        WebDriverWait(self.driver, 60).until(ec.url_contains(QUOTE_URL))

