import pytest
import requests
import random
import string
from Data.data import API
from Data.data import URL


@pytest.fixture
def create_and_delete_courier():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    login_pass.append(login)
    login_pass.append(password)
    login_pass.append(first_name)

    yield login_pass

    response_login_courier = requests.post(f'{URL}{API.login_courier}', data=payload)
    id_courier = response_login_courier.json()['id']

    requests.delete(f'{URL}{API.delete_courier}/{id_courier}')
