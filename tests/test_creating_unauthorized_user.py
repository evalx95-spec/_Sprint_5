from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from ..locators import LoginLocators, AdCreationLocators

class TestAdCreation:
    def test_create_ad_unauthorized(self, driver):
        driver.find_element(*LoginLocators.POST_AD_BUTTON).click()

        wait = WebDriverWait(driver, 5)
        modal_title = wait.until(EC.visibility_of_element_located(AdCreationLocators.MODAL_TITLE))

        assert modal_title.is_displayed() and "Чтобы разместить объявление, авторизуйтесь" in modal_title.text, \
            "Модальное окно не отображается или содержит неверный текст"