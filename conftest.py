import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def driver():
    # Запуск браузера
    browser = webdriver.Chrome()
    
    yield browser
    
    # Завершение работы (закрытие браузера) после окончания теста
    browser.quit()