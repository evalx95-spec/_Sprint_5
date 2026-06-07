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
    POST_AD_BUTTON = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")
    TITLE_INPUT = (By.CSS_SELECTOR, "input[placeholder='Название']")
    DESCRIPTION_TEXTAREA = (By.CSS_SELECTOR, "textarea[placeholder='Описание товара']")
    PRICE_INPUT = (By.CSS_SELECTOR, "input[placeholder='Стоимость']")
    DROPDOWN_CATEGORIES = (By.XPATH, '//input[@name="category"]/following-sibling::button[contains(@class, "dropDownMenu_arrowDown__pfGL1")]')
    SELECT_CATEGORIES = (By.XPATH, "//span[text()='Авто']")
    CITY_DROPDOWN = (By.XPATH, '//input[@name="city"]/following-sibling::button[contains(@class, "dropDownMenu_arrowDown__pfGL1")]')
    SELECT_CITY = (By.XPATH, "//span[text()='Казань']")
    RADIO_BUTTON = By.XPATH, '//input[@type="radio" and @value="Б/У"]'
    PUBLISH_BUTTON = (By.XPATH, "//button[contains(text(), 'Опубликовать')]")
    MY_ADS_BLOCK = (By.XPATH, "//h1[contains(text(), 'Мои объявления')]")
    AD_TITLE = (By.XPATH, "//div[@class='card']//h2")    
