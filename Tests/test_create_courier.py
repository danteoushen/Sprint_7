import allure
import pytest
from conftest import create_and_delete_courier
import requests
from Data.data import API
from Data.data import URL



class TestCourier:
    @allure.title('Проверка успешного создания курьера')
    def test_create_new_courier(self, create_and_delete_courier):
        payload = {"login": create_and_delete_courier[0],
                   "password": create_and_delete_courier[1],
                   "firstName": create_and_delete_courier[2]}
        response = requests.post(f'{URL}{API.create_courier}',
                                 data=payload)
        assert response.status_code == 201
        assert response.json() == {'ok': True}

    @allure.title('Проверка создания курьера с теми же данными')
    def test_create_existing_courier(self, create_and_delete_courier):
        payload = {"login": create_and_delete_courier[0],
                   "password": create_and_delete_courier[1],
                   "firstName": create_and_delete_courier[2]}

        response = requests.post(f'{URL}{API.create_courier}', data=payload)
        assert response.status_code == 201
        assert response.json() == {'ok': True}


        response = requests.post(f'{URL}{API.create_courier}', data=payload)
        assert response.status_code == 409
        assert response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'



    @allure.title('Проверка создания курьера без поля "login"')
    def test_create_new_courier_empty_field(self):
        payload = {
            "password": '123456',
            "firstName": 'Тест'
        }
        response = requests.post(f'{URL}{API.create_courier}',
                                 data=payload)
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'







