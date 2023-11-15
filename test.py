import requests

# URL для отправки запроса
url = 'http://127.0.0.1:5000/get_form'

# Тестовые данные для отправки в запросе
data = {
    'user_name': 'Виктор',
    'order_date': '2022-01-01',
    'lead_email': 'viktor@example.ru',
}

# Отправка POST-запроса с тестовыми данными
response = requests.post(url, data=data)

# Вывод ответа
print(response.json())