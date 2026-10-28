# Sprint_7 Автотесты API для учебного сервиса Яндекс.Самокат

Проект автотестов для учебного API Яндекс Самокат

## Стек
- Python
- requests
- pytest
- allure-pytest
- Faker

## Установка
1. `python -m venv .venv`
2. Активировать окружение
3. `pip install -r requirements.txt`

## Запуск тестов
`pytest --alluredir=allure-results`

## Отчёт Allure
`allure serve allure-results`

## Покрытие
- Создание курьера, проверка дублей, валидация полей
- Авторизация курьера
- Создание заказа (разные варианты цветов самоката)
- Получение списка заказов