from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..locators import LoginLocators, LogoutLocators
from ..user_data import UserData

class TestLogout:

    def test_successful_logout(self, driver):
        email = UserData.USER["email"]
        password = UserData.USER["password"]

        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginLocators.EMAIL_INPUT)
        )
        driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginLocators.SUBMIT_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LogoutLocators.LOGOUT_BUTTON)
        )

        driver.find_element(*LogoutLocators.LOGOUT_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LogoutLocators.LOGIN_BUTTON)
        )

        avatars = driver.find_elements(*LoginLocators.USER_AVATAR)
        user_names = driver.find_elements(*LoginLocators.USER_NAME)
        login_button = driver.find_element(*LogoutLocators.LOGIN_BUTTON)

        assert len(avatars) == 0
        assert len(user_names) == 0
        assert login_button.is_displayed()
        assert "Вход и регистрация" in login_button.text