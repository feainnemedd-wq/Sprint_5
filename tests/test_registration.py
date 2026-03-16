from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from links import Links
from helpers import gen_email, gen_password, gen_name 

class TestRegistration:

    def test_registration_successful(self, driver):
        name = gen_name()
        email = gen_email()
        password = gen_password()

        driver.get(Links.REGISTRATION_PAGE)

        # Регистрация
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION_BUTTON))
        driver.find_element(*Locators.NAME_REGISTRATION_FIELD).send_keys(name)
        driver.find_element(*Locators.EMAIL_REGISTRATION_FIELD).send_keys(email)
        driver.find_element(*Locators.PWD_REGISTRATION_FIELD).send_keys(password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        # Авторизация (вход после регистрации)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.EMAIL_AUTH_FIELD).send_keys(email)
        driver.find_element(*Locators.PWD_AUTH_FIELD).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        assert WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON)
        ).is_displayed()

    def test_registration_short_password_failed(self, driver):
        name = gen_name()
        email = gen_email()
        short_password = '123'

        driver.get(Links.REGISTRATION_PAGE)

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION_BUTTON))
        driver.find_element(*Locators.NAME_REGISTRATION_FIELD).send_keys(name)
        driver.find_element(*Locators.EMAIL_REGISTRATION_FIELD).send_keys(email)
        driver.find_element(*Locators.PWD_REGISTRATION_FIELD).send_keys(short_password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        error_msg = WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.WRONG_PASSWORD_TEXT)
        ).text
        
        assert error_msg == 'Некорректный пароль' and '/register' in driver.current_url