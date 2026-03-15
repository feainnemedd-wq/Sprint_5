from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from links import Links
from locators import Locators

class TestLogout:

    def test_logout_from_profile_success(self, driver, user_data):
        # 1. Регистрация нового пользователя
        driver.get(Links.REGISTRATION_PAGE)
        
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.REGISTRATION_BUTTON))
        driver.find_element(*Locators.NAME_REGISTRATION_FIELD).send_keys(user_data['name'])
        driver.find_element(*Locators.EMAIL_REGISTRATION_FIELD).send_keys(user_data['email'])
        driver.find_element(*Locators.PWD_REGISTRATION_FIELD).send_keys(user_data['password'])
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        # 2. Авторизация (вход)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.EMAIL_AUTH_FIELD).send_keys(user_data['email'])
        driver.find_element(*Locators.PWD_AUTH_FIELD).send_keys(user_data['password'])
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        # 3. Переход в Личный кабинет
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
        driver.find_element(*Locators.PROFILE_LINK).click()

        # 4. Выход из аккаунта
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.EXIT_BUTTON))
        driver.find_element(*Locators.EXIT_BUTTON).click()
        