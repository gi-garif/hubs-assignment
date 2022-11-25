import pytest
from pages.hubs_main_page import HubsMainPage
from pages.order_page import OrderPage
from pages.signup_page import SignUpPage
from test_data.test_data import FILE_STEP, FILE_PNG
from utilities.utils import Utils


@pytest.mark.usefixtures("test_setup")
class TestUpload:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver)
        self.mp = HubsMainPage(self.driver)
        self.op = OrderPage(self.driver)
        self.sp = SignUpPage(self.driver)

    def test_successful_upload(self):
        file_path = FILE_STEP
        self.mp.create_instant_quote()
        self.op.upload_model(file_path)
        self.ut.assert_element_is_enabled(OrderPage.PLACE_ORDER_BTN)

    def test_unsupported_format_upload(self):
        file_path = FILE_PNG
        self.mp.create_instant_quote()
        self.ut.drag_n_drop(self.op.UPLOAD_INPUT, file_path)
        self.ut.assert_element_is_present(self.op.ERROR_MSG)

    def test_successful_upload_with_registration(self):
        file_path = FILE_STEP
        self.mp.register()
        self.sp.signup()
        self.op.upload_model(file_path)
        self.ut.assert_element_is_enabled(OrderPage.PLACE_ORDER_BTN)

