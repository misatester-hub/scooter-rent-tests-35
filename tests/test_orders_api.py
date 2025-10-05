import requests  
from configuration import URL_SERVICE, CREATE_ORDER_PATH, GET_ORDER_PATH


# Кичатов Михаил, 35-я когорта — Финальный проект. Инженер по тестированию плюс
def test_create_and_get_order():
    # 1. Создать заказ
    create_payload = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK"]
    }
    response = requests.post(URL_SERVICE + CREATE_ORDER_PATH, json=create_payload)
    assert response.status_code == 201
    track = response.json()["track"]

    # 2. Получить заказ по треку
    get_response = requests.get(URL_SERVICE + GET_ORDER_PATH, params={"t": track})
    assert get_response.status_code == 200

    # 3. Проверка данных
    order = get_response.json()["order"]
    assert order["firstName"] == "Naruto"
    assert order["lastName"] == "Uchiha"
    assert order["track"] == track
