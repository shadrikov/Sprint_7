import pytest
import requests
from data import *
import allure
from cleanup import CleanUp
import generators

class TestCreateOrder:

    @allure.title('Успешное создание заказа при разных вариантах цвета самоката')
    @pytest.mark.parametrize('color', [
        ['BLACK'],
        ['GREY'],
        ['BLACK','GREY'],
        []
    ])
    def test_create_order_with_colors(self, color):
        payload = generators.order_data_generator(color)
        response = requests.post(
            URLs.CREATE_ORDER_OR_GET_ORDERS_LIST, 
            json=payload
            )
        assert response.status_code == 201
        assert Flags.ORDER_TRACK in response.json()

class TestGetOrdersList:

    @allure.title('Получение списка заказов')
    def test_get_orders_list(self):
        response = requests.get(
            URLs.CREATE_ORDER_OR_GET_ORDERS_LIST
            )
        assert response.status_code == 200
        assert Flags.ORDERS_LIST in response.json()
        assert isinstance(response.json()[Flags.ORDERS_LIST], list)