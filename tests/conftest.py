import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from test_data.test_data import HUBS_MAIN_URL


@pytest.fixture(autouse=True)
def test_setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(HUBS_MAIN_URL)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
