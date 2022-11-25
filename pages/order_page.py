from test_data.test_data import MANUFACTURE_ROOT_URL, ORDER_URL
from utilities.utils import Utils
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class OrderPage:
    UPLOAD_INPUT = "file"
    UPLOAD_EMAIL_FLD = "email"
    UPLOAD_CONFIRM_EMAIL_BTN = "//*[@id='emailWallForm']/div[1]/mat-dialog-actions/button"
    PLACE_ORDER_BTN = "/html/body/h3d-root/h3d-feature-routing-outlet/h3d-router-outlet-template/main/h3d-order-page-v2/h3d-side-panel/mat-sidenav-container/mat-sidenav-content/div[2]/div/div/h3d-order-quote-details-v2/div/h3d-quote-details-v2/div/div[3]/h3d-quote-requirements-editor-v2/div/div[5]/h3d-quote-parts-table-production/div/button"
    TOS_AGREE_BTN = "//*[@id='mat-dialog-0']/h3d-export-control-dialog/button"
    ERROR_MSG = "/html/body/h3d-root/h3d-feature-routing-outlet/h3d-router-outlet-template/main/h3d-new-quote-request/div/div/section[2]/div/h3d-part-upload-area/div/div"

    def __init__(self, driver):
        self.driver = driver

    def upload_model(self, file_path):
        ut = Utils(self.driver)
        ut.drag_n_drop(self.UPLOAD_INPUT, file_path)
        if ut.assert_current_url(MANUFACTURE_ROOT_URL):
            ut.click_by_xpath(self.TOS_AGREE_BTN)
        else:
            ut.enter_text_by_id(self.UPLOAD_EMAIL_FLD, ut.random_email())
            ut.click_by_xpath(self.UPLOAD_CONFIRM_EMAIL_BTN)
        WebDriverWait(self.driver, 60).until(ec.url_contains(ORDER_URL))

