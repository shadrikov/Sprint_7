import pytest
import requests
from data import *
import allure
from cleanup import CleanUp
import generators

class TestCreateCourier:

    @allure.title('Успешное создание курьера')
    def test_create_courier_success(self, courier_data):
        response = requests.post(
            URLs.CREATE_COURIER, 
            data=courier_data
            )
        try:
            assert response.status_code == 201
            assert response.json()['ok'] == True
        finally:
            # Удаляем курьера после теста, предварительно совершив вход в систему и получив id курьера
            CleanUp.delete_courier(courier_data)

    @allure.title('Невозможность создания курьера с повторяющимся логином')
    def test_create_courier_repeating_login_error(self, register_new_courier):
        response = requests.post(
            URLs.CREATE_COURIER, 
            data=register_new_courier
            )
        assert response.status_code == 409
        assert response.json()['message'] == ResponseMessages.CREATE_COURIER_WITH_REPEATING_LOGIN

    @allure.title('Невозможность создания курьера без заполнения обязательных полей')
    @pytest.mark.parametrize('key',['login', 'password', 'firstName'])
    def test_create_courier_missing_required_fields_error(self, key, courier_data):
        # Копируем данные в новую переменную
        incomplete_data = courier_data.copy()
        # Удаляем из словаря один из обязательных ключей
        del incomplete_data[key]

        response = requests.post(
            URLs.CREATE_COURIER, 
            data=incomplete_data
            )
        assert response.status_code == 400
        assert response.json()['message'] == ResponseMessages.CREATE_COURIER_MISSING_REQUIRED_FIELDS

class TestLoginCourier:

    @allure.title('Успешная авторизация курьера')
    def test_login_courier_success(self, register_new_courier):
        payload = {
            'login': register_new_courier['login'],
            'password': register_new_courier['password']
        }
        response = requests.post(
            URLs.LOGIN_COURIER, 
            data=payload
            )
        assert response.status_code == 200
        assert Flags.COURIER_ID in response.json()

    @allure.title('Невозможность авторизации курьера с некорректной парой логин/пароль')
    @pytest.mark.parametrize('key',['login', 'password'])
    def test_login_courier_incorrect_credentials_error(self, key, register_new_courier):
        payload = {
            'login': register_new_courier['login'],
            'password': register_new_courier['password']
        }
        payload[key] = generators.courier_login_generator()
        response = requests.post(
            URLs.LOGIN_COURIER, 
            data=payload
            )
        assert response.status_code == 404
        assert response.json()['message'] == ResponseMessages.LOGIN_COURIER_WITH_INCORRECT_LOGPASSW      

    @allure.title('Невозможность авторизации курьера без заполнения обязательных полей')
    @pytest.mark.parametrize('key',['login', 'password'])
    def test_login_courier_missing_required_fields_error(self, key, register_new_courier):
        payload = {
            'login': register_new_courier['login'],
            'password': register_new_courier['password']
        }
        del payload[key]
        response = requests.post(
            URLs.LOGIN_COURIER, 
            data=payload
            )
        assert response.status_code == 400
        assert response.json()['message'] == ResponseMessages.LOGIN_COURIER_MISSING_REQUIRED_FIELDS        