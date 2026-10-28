import pytest
import generators
import requests
from data import URLs
from cleanup import CleanUp

# Фикстура генерации данных нового курьера
@pytest.fixture
def courier_data():
    courier_data = {
        'login': generators.courier_login_generator(),
        'password': generators.courier_passw_generator(),
        'firstName': generators.courier_name_generator()
    }
    return courier_data

# Фикстура создания нового курьера
@pytest.fixture
def register_new_courier(courier_data):
    # собираем тело запроса
    payload = {
        "login": courier_data['login'],
        "password": courier_data['password'],
        "firstName": courier_data['firstName']
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(
        URLs.CREATE_COURIER, 
        data=payload
        )

    # проверяем, что регистрация прошла успешно
    assert response.status_code == 201, f"Не удалось зарегистрировать курьера: {response.status_code} {response.text}"

    # передаём данные курьера в тест
    yield courier_data 

    # удаляем курьера после теста, предварительно совершив вход в систему и получив id курьера
    CleanUp.delete_courier(courier_data)

        
