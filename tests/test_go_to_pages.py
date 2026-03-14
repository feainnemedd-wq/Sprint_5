import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from links import Links

class TestGoToPage:

    # 1. Тест перехода в Личный кабинет с разных страниц (Главная, Профиль, Лента)
    @pytest.mark.parametrize('page', [Links.START_PAGE, Links.PROFILE_PAGE, Links.FEED_PAGE])
    def test_go_to_profile_page(self, driver, user, page):
        # Переход на страницу регистрации
        driver.get(Links.REGISTRATION_PAGE)
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locators.REGISTRATION_BUTTON))

        # Регистрация
        driver.find_element(*Locators.NAME_REGISTRATION_FIELD).send_keys('Julia')
        driver.find_element(*Locators.EMAIL_REGISTRATION_FIELD).send_keys(user.email)
        driver.find_element(*Locators.PWD_REGISTRATION_FIELD).send_keys(user.password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        # Ожидание перехода на страницу входа
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))

        # Авторизация
        driver.find_element(*Locators.EMAIL_AUTH_FIELD).send_keys(user.email)
        driver.find_element(*Locators.PWD_AUTH_FIELD).send_keys(user.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        # Ожидание выполнения входа
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))

        # Переход на целевую страницу из параметров
        driver.get(page)

        # Клик по кнопке "Личный кабинет" 
        profile_link = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(Locators.PROFILE_LINK))
        driver.execute_script("arguments[0].click();", profile_link)

        # Ждем, когда URL начнет содержать /account (подтверждение перехода)
        WebDriverWait(driver, 20).until(EC.url_contains("/account"))

        # Ждем кнопку "Выход" как гарант полной загрузки профиля
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locators.EXIT_BUTTON))

        # Проверка URL
        assert '/account' in driver.current_url

    # 2. Тест перехода из Личного кабинета обратно в Конструктор
    def test_go_to_constructor_page_from_profile(self, driver, user):
        # Аналогичный процесс входа
        driver.get(Links.REGISTRATION_PAGE)
        driver.find_element(*Locators.NAME_REGISTRATION_FIELD).send_keys('Julia')
        driver.find_element(*Locators.EMAIL_REGISTRATION_FIELD).send_keys(user.email)
        driver.find_element(*Locators.PWD_REGISTRATION_FIELD).send_keys(user.password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.EMAIL_AUTH_FIELD).send_keys(user.email)
        driver.find_element(*Locators.PWD_AUTH_FIELD).send_keys(user.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))

        # Переход в Личный кабинет через JS
        profile_link = driver.find_element(*Locators.PROFILE_LINK)
        driver.execute_script("arguments[0].click();", profile_link)
        
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locators.EXIT_BUTTON))

        # Клик по кнопке "Конструктор"
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

        # Ожидание заголовка на главной странице
        title_element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locators.TITLE))

        # Проверка текста заголовка
        assert title_element.text == 'Соберите бургер'