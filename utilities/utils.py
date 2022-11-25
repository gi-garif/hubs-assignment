import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Utils:
    def __init__(self, driver):
        self.driver = driver

    def assert_element_is_present(self, element_id):
        element = self.driver.find_element(By.XPATH, element_id)
        assert element.is_displayed()

    def assert_element_is_enabled(self, element_id):
        element = self.driver.find_element(By.XPATH, element_id)
        assert element.is_enabled()

    def drag_n_drop(self, element_id, file_path):
        WebDriverWait(self.driver, 30).until(ec.presence_of_element_located((By.ID, element_id)))
        element = self.driver.find_element(By.ID, element_id)
        element.send_keys(file_path)

    def enter_text_by_id(self, element_id, text):
        element = self.driver.find_element(By.ID, element_id)
        element.send_keys(text)

    def click_by_id(self, element_id):
        element = self.driver.find_element(By.ID, element_id)
        element.click()

    def click_by_xpath(self, element_xp):
        element = self.driver.find_element(By.XPATH, element_xp)
        element.click()

    def click_by_id_js(self, element_id):
        element = self.driver.find_element(By.ID, element_id)
        self.driver.execute_script("arguments[0].click()", element)

    def click_by_css_js(self, element_css):
        element = self.driver.find_element(By.CSS_SELECTOR, element_css)
        self.driver.execute_script("arguments[0].click()", element)

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    def assert_current_url(self, url):
        current_url = self.driver.current_url
        return current_url == url

    def random_value(self, length):
        pwd = ''
        while len(pwd) != length:
            pwd += random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
        return pwd

    def random_word(self, length):
        return "".join(random.choice(string.ascii_letters) for _ in range(length))

    def random_email(self):
        return self.random_word(8) + "@mail.com"
