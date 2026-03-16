from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from links import Links
from helpers import gen_email, gen_password, gen_name 

class TestLogin:

    def test_login_button_from_main_page(self, driver):
        driver.get(Links.START_PAGE)
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(Locators.LOGIN_BUTTON_FROM_MAIN_PAGE)
        ).click()
        
        assert WebDriverWait(driver, 10).until(expected_conditions.url_contains('/login'))

    def test_login_button_from_profile(self, driver):
        driver.get(Links.START_PAGE)
        driver.find_element(*Locators.PROFILE_LINK).click()
        
        assert WebDriverWait(driver, 10).until(expected_conditions.url_contains('/login'))

    def test_login_button_registration_page(self, driver):
        driver.get(Links.REGISTRATION_PAGE)
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(Locators.LOGIN_LINK)
        ).click()
        
        assert WebDriverWait(driver, 10).until(expected_conditions.url_contains('/login'))

    def test_login_success(self, driver):
        name = gen_name()
        email = gen_email()
        password = gen_password()

        # Регистрация 
        driver.get(Links.REGISTRATION_PAGE)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION_BUTTON))
        
        driver.find_element(*Locators.NAME_REGISTRATION_FIELD).send_keys(name)
        driver.find_element(*Locators.EMAIL_REGISTRATION_FIELD).send_keys(email)
        driver.find_element(*Locators.PWD_REGISTRATION_FIELD).send_keys(password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        # Авторизация
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.EMAIL_AUTH_FIELD).send_keys(email)
        driver.find_element(*Locators.PWD_AUTH_FIELD).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        # Переход в Личный кабинет 
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
        driver.find_element(*Locators.PROFILE_LINK).click()

        assert WebDriverWait(driver, 10).until(
            expected_conditions.url_contains('/account')
        )