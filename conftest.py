import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urls import Urls


@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(Urls.HOME_PAGE)
    yield driver
    driver.quit()