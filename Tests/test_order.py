import allure
import pytest
import requests
import json
from Data.data import DataOrder
from Data.data import API
from Data.data import URL

class TestOrder:
    @allure.title('Проверка создания заказа со скутерами разных цветов и что в ответе содержится "track"')
    @pytest.mark.parametrize('color',
                             [
                                 DataOrder.COLOR_BLACK,
                                 DataOrder.COLOR_GREY,
                                 DataOrder.WITHOUT_COLOR,
                                 DataOrder.BOTH_COLORS
                             ]
                             )
    def test_create_order_with_color(self, color):
        DataOrder = json.dumps(color)
        response = requests.post(f'{URL}{API.create_order}', data=DataOrder)
        assert response.status_code == 201
        assert 'track' in response.text


class TestOrderList:
    def test_get_list(self):
        response = requests.get(f'{URL}{API.create_order}')
        assert response.status_code == 200
        assert type(response.json()['orders']) == list