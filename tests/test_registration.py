from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from links import Links

class TestRegistration:

    def test_registration_successful(self, driver, user_data):
        driver.get(Links.REGISTRATION_PAGE)

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION_BUTTON))
        driver.find_element(*Locators.NAME_REGISTRATION_FIELD).send_keys(user_data['name'])
        driver.find_element(*Locators.EMAIL_REGISTRATION_FIELD).send_keys(user_data['email'])
        driver.find_element(*Locators.PWD_REGISTRATION_FIELD).send_keys(user_data['password'])
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.EMAIL_AUTH_FIELD).send_keys(user_data['email'])
        driver.find_element(*Locators.PWD_AUTH_FIELD).send_keys(user_data['password'])
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        assert WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON)
        ).is_displayed()

    def test_registration_short_password_failed(self, driver, user_data):
        driver.get(Links.REGISTRATION_PAGE)

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION_BUTTON))
        driver.find_element(*Locators.NAME_REGISTRATION_FIELD).send_keys(user_data['name'])
        driver.find_element(*Locators.EMAIL_REGISTRATION_FIELD).send_keys(user_data['email'])
        short_password = '123'
        driver.find_element(*Locators.PWD_REGISTRATION_FIELD).send_keys(short_password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        error_msg = WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.WRONG_PASSWORD_TEXT)
        ).text
        
        assert error_msg == 'Некорректный пароль' and '/register' in driver.current_url