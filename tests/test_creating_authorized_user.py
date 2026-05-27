import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators import LOGIN, AD_CREATION

def create_ad(driver, email, password, title, description, price, category, city, condition):
    wait = WebDriverWait(driver, 10)

    login_button = wait.until(EC.element_to_be_clickable(LOGIN['login_button']))
    login_button.click()

    email_input = wait.until(EC.visibility_of_element_located(LOGIN['email_input']))
    email_input.send_keys(email)

    password_input = driver.find_element(*LOGIN['password_input'])
    password_input.send_keys(password)

    submit_button = driver.find_element(*LOGIN['submit_button'])
    submit_button.click()

    wait.until(EC.visibility_of_element_located(LOGIN['user_avatar']))

    post_ad_button = wait.until(EC.element_to_be_clickable(LOGIN['post_ad_button']))
    post_ad_button.click()

    title_input = wait.until(EC.visibility_of_element_located(AD_CREATION['title_input']))
    title_input.send_keys(title)

    description_input = driver.find_element(*AD_CREATION['description_input'])
    description_input.send_keys(description)

    price_input = driver.find_element(*AD_CREATION['price_input'])
    price_input.send_keys(str(price))

    category_dropdown = driver.find_element(*AD_CREATION['category_dropdown'])
    category_option = category_dropdown.find_element(By.XPATH, f".//option[@value='{category}']")
    category_option.click()

    city_dropdown = driver.find_element(*AD_CREATION['city_dropdown'])
    city_option = city_dropdown.find_element(By.XPATH, f".//option[@value='{city}']")
    city_option.click()

    condition_radio = driver.find_elements(*AD_CREATION['condition_radio'])
    for radio in condition_radio:
        if radio.get_attribute("value") == condition:
            radio.click()
            break

    
    publish_button = driver.find_element(*AD_CREATION['publish_button'])
    publish_button.click()

    
    user_avatar = wait.until(EC.element_to_be_clickable(LOGIN['user_avatar']))
    user_avatar.click()

    
    my_ads_section = wait.until(EC.visibility_of_element_located(AD_CREATION['my_ads_section']))
    ad_titles = my_ads_section.find_elements(*AD_CREATION['ad_title_in_list'])
    ad_found = any(title in ad.text for ad in ad_titles)

    assert ad_found, f"Объявление с названием '{title}' не найдено в списке 'Мои объявления'"
    print(f"Объявление '{title}' успешно создано и отображается в профиле.")

class TestCreateAdvertisement:
    def test_create_advertisement_authorized_user(self, driver):
       
        email = "evgeniya_kozlova_1995@mail.ru"
        password = "123456"
        ad_title = "Тестовый товар для продажи"

        try:
            create_ad(
                driver=driver,
                email=email,
                password=password,
                title=ad_title,
                description="Подробное описание тестового товара",
                price=5000,
                category="Авто",
                city="Москва",
                condition="Новый"
            )
        except TimeoutException as e:
            pytest.fail(f"Превышение времени ожидания: {e}")
        except Exception as e:
            pytest.fail(f"Ошибка при выполнении теста: {e}")
   