import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from links import Links

class TestConstructor:

    def test_ingredients_switch_buns(self, driver):
        driver.get(Links.START_PAGE)

        # Сначала переключаемся на "Начинки", чтобы "Булки" перестали быть активными
        driver.find_element(*Locators.FILLINGS_INGREDIENTS).click()
        
        # Теперь переключаемся обратно на "Булки"
        element = driver.find_element(*Locators.BUNS_INGREDIENTS)
        element.click()

        assert WebDriverWait(driver, 10).until(
            lambda d: 'current' in element.get_attribute('class')
        )

    @pytest.mark.parametrize('ingredient', [
        Locators.SAUCES_INGREDIENTS,
        Locators.FILLINGS_INGREDIENTS
    ])
    def test_ingredients_switcher(self, driver, ingredient):
        driver.get(Links.START_PAGE)

        # Находим нужный раздел и кликаем
        element = driver.find_element(*ingredient)
        element.click()

        assert WebDriverWait(driver, 10).until(
            lambda d: 'current' in element.get_attribute('class')
        )