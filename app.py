from flask import Flask, request, jsonify
from tinydb import TinyDB

app = Flask(__name__)

# Инициализация базы данных
db = TinyDB('database.json')

# Функция для динамической типизации полей на лету
def infer_field_type(value):
    # Валидация даты
    try:
        if '.' in value:
            day, month, year = map(int, value.split('.'))
        else:
            year, month, day = map(int, value.split('-'))
        return "date"
    except ValueError:
        pass

    # Валидация телефона
    if value.startswith('+7') and len(value) == 16 and value[3:].replace(" ", "").isdigit():
        return "phone"

    # Валидация email
    if '@' in value and '.' in value:
        return "email"

    # По умолчанию считаем текстом
    return "text"

# Обработка POST запроса
@app.route('/get_form', methods=['POST'])
def get_form():
    data = request.form
    print(data)
    fields = {key: data[key] for key in data.keys()}

    # Поиск подходящего шаблона
    for template in db.all():
        template_fields = {key: template[key] for key in template.keys() if key != "name"}
        field_types = {key: infer_field_type(value) for key, value in fields.items()}

        if all(field in field_types.values() for field in template_fields.values()):
            return jsonify({"template_name": template["name"]})

    return jsonify(field_types)

if __name__ == '__main__':
    app.run(debug=True)
