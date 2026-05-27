from selenium.webdriver.common.by import By


class LoginLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[placeholder='Введите Email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[placeholder='Пароль']")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    USER_AVATAR = (By.CLASS_NAME, "circleSmall")
    USER_NAME = (By.CLASS_NAME, "profileText")
    POST_AD_BUTTON = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")


class RegistrationLocators:
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[placeholder='Введите Email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[placeholder='Пароль']")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[placeholder='Повторите пароль']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")



class LogoutLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти')]")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")


class AdCreationLocators:
    MODAL_TITLE = (By.XPATH, "//h1[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]")