class URLs:

    MAIN_URL = 'https://qa-scooter.praktikum-services.ru/'
    
    CREATE_COURIER = f'{MAIN_URL}api/v1/courier'

    LOGIN_COURIER = f'{MAIN_URL}api/v1/courier/login'

    @staticmethod
    def delete_courier_handle(courier_id):
        DELETE_COURIER = f'{URLs.MAIN_URL}api/v1/courier/{courier_id}'
        return DELETE_COURIER

    CREATE_ORDER_OR_GET_ORDERS_LIST = f'{MAIN_URL}api/v1/orders'

class ResponseMessages:
    # Ожидаемые сообщения в ответах API
    CREATE_COURIER_MISSING_REQUIRED_FIELDS = 'Недостаточно данных для создания учетной записи'
    CREATE_COURIER_WITH_REPEATING_LOGIN = 'Этот логин уже используется'
    LOGIN_COURIER_MISSING_REQUIRED_FIELDS = 'Недостаточно данных для входа'
    LOGIN_COURIER_WITH_INCORRECT_LOGPASSW = 'Учетная запись не найдена'

class Flags:
    # Флаги для проверки успешных операций
    COURIER_ID = 'id'
    ORDER_TRACK = 'track'
    ORDERS_LIST = 'orders'
    ORDER_ID = 'id'
