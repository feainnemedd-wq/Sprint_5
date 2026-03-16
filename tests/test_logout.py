from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from links import Links
from locators import Locators
from helpers import gen_email, gen_password, gen_name 

class TestLogout:

    def test_logout_from_profile_success(self, driver):
        # 1. Генерация данных пользователя
        name = gen_name()
        email = gen_email()
        password = gen_password()

        # 2. Регистрация
        driver.get(Links.REGISTRATION_PAGE)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.REGISTRATION_BUTTON))
        driver.find_element(*Locators.NAME_REGISTRATION_FIELD).send_keys(name)
        driver.find_element(*Locators.EMAIL_REGISTRATION_FIELD).send_keys(email)
        driver.find_element(*Locators.PWD_REGISTRATION_FIELD).send_keys(password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        # 3. Авторизация (вход)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.EMAIL_AUTH_FIELD).send_keys(email)
        driver.find_element(*Locators.PWD_AUTH_FIELD).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        # 4. Переход в личный кабинет
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
        driver.find_element(*Locators.PROFILE_LINK).click()

        # 5. Выход из аккаунта
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.EXIT_BUTTON))
        driver.find_element(*Locators.EXIT_BUTTON).click()

        assert WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON)
        ).is_displayed()
        