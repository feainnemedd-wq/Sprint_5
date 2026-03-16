import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from links import Links
from helpers import gen_email, gen_password, gen_name 

class TestGoToPage:

    @pytest.mark.parametrize('page', [Links.START_PAGE, Links.FEED_PAGE])
    def test_go_to_profile_page(self, driver, page):
        name = gen_name()
        email = gen_email()
        password = gen_password()

        # Регистрация
        driver.get(Links.REGISTRATION_PAGE)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.REGISTRATION_BUTTON))
        driver.find_element(*Locators.NAME_REGISTRATION_FIELD).send_keys(name)
        driver.find_element(*Locators.EMAIL_REGISTRATION_FIELD).send_keys(email)
        driver.find_element(*Locators.PWD_REGISTRATION_FIELD).send_keys(password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        # Авторизация (вход)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.EMAIL_AUTH_FIELD).send_keys(email)
        driver.find_element(*Locators.PWD_AUTH_FIELD).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        # 2. Переход на страницу из параметров и клик в Личный кабинет
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        driver.get(page)
        
        # Клик по ссылке профиля
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.PROFILE_LINK)).click()

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.EXIT_BUTTON)
        ).is_displayed()

    def test_go_to_constructor_page_from_profile(self, driver):
        name = gen_name()
        email = gen_email()
        password = gen_password()

        # Вход в аккаунт через регистрацию
        driver.get(Links.REGISTRATION_PAGE)
        driver.find_element(*Locators.NAME_REGISTRATION_FIELD).send_keys(name)
        driver.find_element(*Locators.EMAIL_REGISTRATION_FIELD).send_keys(email)
        driver.find_element(*Locators.PWD_REGISTRATION_FIELD).send_keys(password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.EMAIL_AUTH_FIELD).send_keys(email)
        driver.find_element(*Locators.PWD_AUTH_FIELD).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        # Переход в Личный кабинет
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        driver.find_element(*Locators.PROFILE_LINK).click()
        
        # Ждем загрузку профиля и кликаем в Конструктор
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.EXIT_BUTTON))
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.TITLE)
        ).text == 'Соберите бургер'