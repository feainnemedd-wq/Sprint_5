import pytest
from helpers import gen_password, gen_email, gen_name

@pytest.fixture(scope='function')
def user_data():
    return {
        "name": gen_name(),
        "email": gen_email(),
        "password": gen_password()
    }
