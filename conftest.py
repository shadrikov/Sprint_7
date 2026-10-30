import pytest
import generators
import requests
import allure
from data import Flags
from cleanup import CleanUp
from api_client import ApiClient

# Фикстура генерации данных нового курьера
@pytest.fixture
def courier_data():
    courier_data = {
        'login': generators.courier_login_generator(),
        'password': generators.courier_passw_generator(),
        'firstName': generators.courier_name_generator()
    }
    return courier_data

# Фикстура-фабрика создания нового курьера и удаления её после теста
@pytest.fixture
def create_new_courier():
    courier_ids = []

    def _create(payload):
        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = ApiClient.post_request_create_courier(payload)

        if response.status_code != 201:
            allure.attach(
                body=response.text,
                name=f"Не удалось зарегистрировать курьера: статус {response.status_code}",
                attachment_type=allure.attachment_type.TEXT
            )

        # вход в систему и получение id курьера
        login_payload = {
            "login": payload['login'],
            "password": payload['password']
        }

        response_login = ApiClient.post_request_login_courier(login_payload)

        # получаем id курьера и добавляем его в список
        courier_id = response_login.json().get(Flags.COURIER_ID)
        if courier_id:
            courier_ids.append(courier_id)
        
        # возвращаем в тест ответ на запрос создания курьера
        return response

    # передаём функцию создания курьера в тест
    yield _create 

    # удаляем курьеров после теста
    for courier_id in courier_ids:
        CleanUp.delete_courier(courier_id)      

# Фикстура удаления курьера после теста
@pytest.fixture
def cleanup_courier():
    courier_ids = []

    def get_id(payload):

        # вход в систему и получение id курьера для последующего удаления
        login_payload = {
            "login": payload['login'],
            "password": payload['password']
        }

        response_login = ApiClient.post_request_login_courier(login_payload)

        # получаем id курьера и добавляем его в список
        courier_id = response_login.json().get(Flags.COURIER_ID)
        if courier_id:
            courier_ids.append(courier_id)
        
        # возвращаем в тест ответ на запрос авторизации курьера
        return response_login

    # передаём функцию авторизации и получения id курьера в тест
    yield get_id 

    # удаляем курьеров после теста
    for courier_id in courier_ids:
        CleanUp.delete_courier(courier_id)      
