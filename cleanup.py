import requests
from data import URLs
import allure

class CleanUp:

    @staticmethod
    # Функция удаления курьера 
    def delete_courier(courier_data):
        
        # удаляем курьера после теста, предварительно совершив вход в систему и получив id курьера
        login_payload = {
            "login": courier_data['login'],
            "password": courier_data['password']
        }
    
        response_login = requests.post(
                    URLs.LOGIN_COURIER, 
                    data=login_payload
                    )
        
        courier_id = None
    
        if response_login.status_code == 200:
            courier_id = response_login.json().get("id")
    
        if courier_id is not None:
            delete_url = URLs.delete_courier_handle('')
            response_delete = requests.delete(delete_url)
            if response_delete.status_code != 200:
                allure.attach(
                    body=response_delete.text,
                    name=f"Не удалось удалить курьера {courier_id}: статус {response_delete.status_code}",
                    attachment_type=allure.attachment_type.TEXT
                )
        else:
            allure.attach(
                body=response_login.text,
                name=f"Не удалось получить id курьера для удаления: статус {response_login.status_code}",
                attachment_type=allure.attachment_type.TEXT
            )