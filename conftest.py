import random
import pytest
from selenium import webdriver
import helpers
from data import User

@pytest.fixture(scope='function')
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1024,768')
    
    driver = webdriver.Chrome(options=chrome_options)
    
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def user():
    user = User(name='Julia')
    user.email = f'julia_pozdnyakova_41{random.randint(1000, 9999)}@autotest.ru'
    user.password = helpers.gen_password()
    return user