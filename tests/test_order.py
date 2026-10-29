import pytest
import requests
from data import *
import allure
from cleanup import CleanUp
import generators
from api_client import ApiClient

class TestCreateOrder:

    @allure.title('Успешное создание заказа при разных вариантах цвета самоката')
    @pytest.mark.parametrize('color', [
        ['BLACK'],
        ['GREY'],
        ['BLACK','GREY'],
        []
    ])
    def test_create_order_with_colors(self, color):
        response = ApiClient.post_request_create_order(color)
        assert response.status_code == 201
        assert Flags.ORDER_TRACK in response.json()

class TestGetOrdersList:

    @allure.title('Получение списка заказов')
    def test_get_orders_list(self):
        response = ApiClient.get_request_get_orders()
        assert response.status_code == 200
        assert Flags.ORDERS_LIST in response.json()
        assert isinstance(response.json()[Flags.ORDERS_LIST], list)