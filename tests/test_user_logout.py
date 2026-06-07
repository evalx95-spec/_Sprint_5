from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from ..locators import LoginLocators, LogoutLocators

class TestLogout:
    
    def test_successful_logout(self, driver):
        email = "evgeniya_kozlova_1995@mail.ru"
        password = "12356"
        
        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
        try:
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
        except TimeoutException as e:
            raise AssertionError(f"Timeout while waiting for element: {e}")
        
        avatars = driver.find_elements(*LoginLocators.USER_AVATAR)
        user_names = driver.find_elements(*LoginLocators.USER_NAME)
        login_button = driver.find_element(*LogoutLocators.LOGIN_BUTTON)
        
        assert len(avatars) == 0, "Аватар пользователя всё ещё отображается"
        assert len(user_names) == 0, "Имя пользователя всё ещё отображается"
        assert login_button.is_displayed(), "Кнопка входа не отображается"
        assert "Вход и регистрация" in login_button.text, "Текст кнопки входа не соответствует ожидаемому"