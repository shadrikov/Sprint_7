import requests
from data import URLs
import allure

class CleanUp:

    @staticmethod
    # Функция удаления курьера 
    def delete_courier(courier_id):
        delete_url = URLs.delete_courier_handle(courier_id)
        response_delete = requests.delete(delete_url)
        if response_delete.status_code != 200:
            allure.attach(
                body=response_delete.text,
                name=f"Не удалось удалить курьера {courier_id}: статус {response_delete.status_code}",
                attachment_type=allure.attachment_type.TEXT
            )
            