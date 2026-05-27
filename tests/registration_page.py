from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..locators import LoginLocators, RegistrationLocators

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_registration(self):
        
        self.driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
        self.wait.until(
            EC.element_to_be_clickable(RegistrationLocators.NO_ACCOUNT_BUTTON)
        )
        self.driver.find_element(*RegistrationLocators.NO_ACCOUNT_BUTTON).click()

    def fill_registration_form(self, email, password):
       
        self.driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*RegistrationLocators.CONFIRM_PASSWORD_INPUT).send_keys(password)

    def submit_registration(self):
      
        self.driver.find_element(*RegistrationLocators.CREATE_ACCOUNT_BUTTON).click()

    def wait_for_registration_completion(self):
        
        self.wait.until(
            EC.presence_of_element_located(LoginLocators.POST_AD_BUTTON)
        )
        self.wait.until(
            EC.presence_of_element_located(LoginLocators.USER_AVATAR)
        )

    def get_user_avatar(self):
        return self.driver.find_element(*LoginLocators.USER_AVATAR)

    def get_user_name(self):
        return self.driver.find_element(*LoginLocators.USER_NAME)
