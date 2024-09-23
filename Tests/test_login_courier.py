import allure
import pytest
from conftest import create_and_delete_courier
import allure
import requests
from Data.data import API
from Data.data import URL


class TestLoginCourier:
    @allure.title('Проверка, что курьер может авторизоваться и в ответ пришел id')
    def test_login_courier(self, create_and_delete_courier):

        payload = {"login": create_and_delete_courier[0],
                   "password": create_and_delete_courier[1],
                   "firstName": create_and_delete_courier[2]}

        requests.post(f'{URL}{API.create_courier}',
                      data=payload)


        response = requests.post(f'{URL}{API.login_courier}',
                                 data=payload)

        assert response.status_code == 200
        assert response.json() == {'id': response.json()['id']}


    @allure.title('Проверка, что курьер не может авторизоваться с путым полем "login"')
    def test_login_courier_without_login(self, create_and_delete_courier):

        payload = {"login": create_and_delete_courier[0],
                   "password": create_and_delete_courier[1],
                   "firstName": create_and_delete_courier[2]}

        requests.post(f'{URL}{API.create_courier}', data=payload)

        payload = {"login": '',
                   "password": create_and_delete_courier[1],
                   "firstName": create_and_delete_courier[2]}

        response = requests.post(f'{URL}{API.login_courier}',
                                 data=payload)


        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для входа'


    @allure.title('Проверка, что курьер не может авторизоваться с несуществующим логином"')
    def test_login_courier_with_wrong_login(self, create_and_delete_courier):

        payload = {"login": create_and_delete_courier[0],
                   "password": create_and_delete_courier[1],
                   "firstName": create_and_delete_courier[2]}

        requests.post(f'{URL}{API.create_courier}', data=payload)

        payload = {"login": '123456789',
                   "password": create_and_delete_courier[1],
                   "firstName": create_and_delete_courier[2]}


        response = requests.post(f'{URL}{API.login_courier}',
                                 data=payload)

        assert response.status_code == 404
        assert response.json()['message'] == 'Учетная запись не найдена'



