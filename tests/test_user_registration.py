import pytest
import time
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..locators import LoginLocators, RegistrationLocators # Предполагается, что locators.py существует


class TestRegistration:

    TEST_PASSWORD = "Test123456"

    @staticmethod
    def generate_email():
    
        timestamp = int(time.time() * 1000)
        random_num = random.randint(1, 9999)
        return f"testuser_{timestamp}_{random_num}@example.com"

    def test_successful_registration(self, driver):
        
        email = self.generate_email()
        password = self.TEST_PASSWORD

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginLocators.LOGIN_BUTTON)
        )
        login_button.click()

        no_account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationLocators.NO_ACCOUNT_BUTTON)
        )
        no_account_button.click()

        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationLocators.EMAIL_INPUT)
        )
        email_input.send_keys(email)

        password_input = driver.find_element(*RegistrationLocators.PASSWORD_INPUT)
        password_input.send_keys(password)

        confirm_password_input = driver.find_element(*RegistrationLocators.CONFIRM_PASSWORD_INPUT)
        confirm_password_input.send_keys(password)
        create_account_button = driver.find_element(*RegistrationLocators.CREATE_ACCOUNT_BUTTON)
        create_account_button.click()

        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginLocators.POST_AD_BUTTON),
            "Кнопка 'Post Ad' не появилась после регистрации"
        )
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginLocators.USER_AVATAR),
            "Аватар пользователя не появился после регистрации"
        )

        avatar = driver.find_element(*LoginLocators.USER_AVATAR)
        user_name = driver.find_element(*LoginLocators.USER_NAME)

        assert avatar.is_displayed(), "Аватар пользователя не отображается"
        assert user_name.is_displayed(), "Имя пользователя не отображается"
        assert "User" in user_name.text, f"Ожидалось 'User' в тексте имени пользователя, получено: {user_name.text}"