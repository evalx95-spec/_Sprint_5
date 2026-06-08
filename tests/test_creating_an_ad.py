from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from ..locators import LoginLocators, AdCreationLocators
from ..user_data import UserData

class TestAdCreation:

    def test_create_ad_unauthorized(self, driver):

        driver.find_element(*LoginLocators.POST_AD_BUTTON).click()

        wait = WebDriverWait(driver, 5)

        assert wait.until(EC.visibility_of_element_located(AdCreationLocators.MODAL_TITLE))

    def test_create_ad_authorized(self, driver):
        email = UserData.USER["email"]
        password = UserData.USER["password"]
        wait = WebDriverWait(driver, 10)

        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
        wait.until(
            EC.presence_of_element_located(LoginLocators.EMAIL_INPUT)
        )
        driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginLocators.SUBMIT_BUTTON).click()

        wait.until(
            EC.visibility_of_element_located(LoginLocators.USER_AVATAR))
        driver.find_element(*AdCreationLocators.POST_AD_BUTTON).click()

        driver.find_element(*AdCreationLocators.TITLE_INPUT).send_keys(UserData.AD_DATA["title"])
        driver.find_element(*AdCreationLocators.DESCRIPTION_TEXTAREA).send_keys(UserData.AD_DATA["description"])
        driver.find_element(*AdCreationLocators.PRICE_INPUT).send_keys(UserData.AD_DATA["price"])

        driver.find_element(*AdCreationLocators.DROPDOWN_CATEGORIES).click()
        driver.find_element(*AdCreationLocators.SELECT_CATEGORIES).click()

        driver.find_element(*AdCreationLocators.CITY_DROPDOWN).click()
        driver.find_element(*AdCreationLocators.SELECT_CITY).click()

        radio_button = wait.until(EC.presence_of_element_located(AdCreationLocators.RADIO_BUTTON))
        driver.execute_script("arguments[0].scrollIntoView(true);", radio_button)
        driver.execute_script("arguments[0].click();", radio_button)

        driver.find_element(*AdCreationLocators.PUBLISH_BUTTON).click()

        wait.until(
            EC.visibility_of_element_located(LoginLocators.USER_AVATAR))

        driver.find_element(*LoginLocators.USER_AVATAR).click()


        wait.until(
             EC.presence_of_element_located(AdCreationLocators.MY_ADS_BLOCK))

        ad_title_element = driver.find_element(*AdCreationLocators.AD_TITLE)

        tit = UserData.AD_DATA["title"]
        assert tit in ad_title_element.text