import requests
from data import URLs

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
            delete_url = URLs.delete_courier_handle(courier_id)
            response_delete = requests.delete(delete_url)
            if response_delete.status_code != 200:
                print(f"Не удалось удалить курьера {courier_id}: {response_delete.status_code} {response_delete.text}")
        else:
            print(f"Не удалось получить id курьера для удаления: {response_login.status_code} {response_login.text}")