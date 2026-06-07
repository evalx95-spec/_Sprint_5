from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..locators import LoginLocators

class TestLogin:
    def test_successful_login(self, driver, valid_user):
        email = valid_user["email"]
        password = valid_user["password"]

        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginLocators.EMAIL_INPUT)
        )
        driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginLocators.SUBMIT_BUTTON).click()

        wait = WebDriverWait(driver, 10)

        assert wait.until(EC.visibility_of_element_located(LoginLocators.POST_AD_BUTTON)), \
            "Кнопка 'Разместить объявление' не отображается после входа"

        avatar = wait.until(EC.visibility_of_element_located(LoginLocators.USER_AVATAR))
        assert avatar.is_displayed(), "Аватар пользователя не отображается"

        user_name_element = wait.until(EC.visibility_of_element_located(LoginLocators.USER_NAME))
        assert user_name_element.is_displayed(), "Имя пользователя не отображается"
        assert valid_user["expected_username_part"] in user_name_element.text, \
            f"Имя пользователя не содержит '{valid_user['expected_username_part']}', фактическое: '{user_name_element.text}'"