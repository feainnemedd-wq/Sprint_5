import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from links import Links


class TestGoToPage:

    @pytest.mark.parametrize('page', [Links.START_PAGE, Links.PROFILE_PAGE, Links.FEED_PAGE])
    def test_go_to_profile_page(self, driver, user, page):

        # переход на страницу регистрации пользователя
        driver.get(Links.REGISTRATION_PAGE)

        # ожидание загрузки страницы пока не появится кнопка "Зарегистрироваться"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION_BUTTON))

        # регистрация пользователя
class User:

    def __init__(self, name):
        self.__name = name
        self.__email = None
        self.__password = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password
        