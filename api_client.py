import requests
from data import URLs
import generators
import allure

class ApiClient:
    @staticmethod
    @allure.step("Отправляем POST-запрос на создание курьера")
    def post_request_create_courier(payload):
        url = URLs.CREATE_COURIER
        return requests.post(url, data=payload)

    @staticmethod
    @allure.step("Отправляем POST-запрос на авторизацию курьера")
    def post_request_login_courier(payload):
        url = URLs.LOGIN_COURIER
        return requests.post(url, data=payload)

    @staticmethod
    @allure.step("Отправляем POST-запрос на создание заказа")
    def post_request_create_order(color):
        url = URLs.CREATE_ORDER_OR_GET_ORDERS_LIST
        payload = generators.order_data_generator(color)
        return requests.post(url, json=payload)

    @staticmethod
    @allure.step("Отправляем GET-запрос на получение списка заказов")
    def get_request_get_orders():
        url = URLs.CREATE_ORDER_OR_GET_ORDERS_LIST
        return requests.get(url)
