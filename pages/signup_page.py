from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from test_data.test_data import SIGN_UP_URL, MANUFACTURE_ROOT_URL
from utilities.utils import Utils


class SignUpPage:
    FIRST_NAME_FLD = "sign-up-form__first-name"
    SELECT_FILES_BTN = "file-btn"
    LAST_NAME_FLD = "sign-up-form__last-name"
    EMAIL_FLD = "sign-up-form__email"
    PASSWORD_FLD = "password-macher__password"
    CONFIRM_PASSWORD_FLD = "password-macher__password-confirm"
    TERMS_OF_USE_CHK = "sign-up-form__accept-tos-input"
    RECAPTCHA_CHK = "//*[@id='recaptcha-anchor']"
    SIGN_UP_BTN = "#sign-up-form__sign-up-button"

    def __init__(self, driver):
        self.driver = driver

    def signup(self):
        ut = Utils(self.driver)
        WebDriverWait(self.driver, 60).until(ec.url_to_be(SIGN_UP_URL))

        ut.enter_text_by_id(self.FIRST_NAME_FLD, ut.random_word(5))
        ut.enter_text_by_id(self.LAST_NAME_FLD, ut.random_word(5))
        ut.enter_text_by_id(self.EMAIL_FLD, ut.random_email())
        value = ut.random_value(8)
        ut.enter_text_by_id(self.PASSWORD_FLD, value)
        ut.enter_text_by_id(self.CONFIRM_PASSWORD_FLD, value)
        ut.click_by_id_js(self.TERMS_OF_USE_CHK)
        ut.scroll_to_bottom()
        WebDriverWait(self.driver, 90).until(ec.frame_to_be_available_and_switch_to_it(
            (By.CSS_SELECTOR, "iframe[src^='https://www.google.com/recaptcha/api2/anchor']")))
        WebDriverWait(self.driver, 90).until(ec.element_to_be_clickable((By.XPATH, self.RECAPTCHA_CHK))).click()
        self.driver.switch_to.default_content()
        WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.SIGN_UP_BTN)))
        ut.click_by_css_js(self.SIGN_UP_BTN)
        WebDriverWait(self.driver, 60).until(ec.url_to_be(MANUFACTURE_ROOT_URL))

