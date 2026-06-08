import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..locators import LoginLocators, RegistrationLocators
from ..generate_email import generate_email

class TestRegistration:

    def test_successful_registration(self, driver):
        email = generate_email()
        password = "test12345"

        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationLocators.NO_ACCOUNT_BUTTON)
        )
        driver.find_element(*RegistrationLocators.NO_ACCOUNT_BUTTON).click()

        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationLocators.CONFIRM_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationLocators.CREATE_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginLocators.POST_AD_BUTTON)
        )
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginLocators.USER_AVATAR)
        )

        avatar = driver.find_element(*LoginLocators.USER_AVATAR)
        user_name = driver.find_element(*LoginLocators.USER_NAME)

        assert avatar.is_displayed()
        assert user_name.is_displayed()
        assert "User" in user_name.text