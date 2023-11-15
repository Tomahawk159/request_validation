# validation_request

## Установка
Клонировать этот репозиторий. `git clone https://github.com/Tomahawk159/validation_request`

## Запуск 
1. Создание виртуального окружения `python -m venv venv`
2. Активация вирт окружения для Win `venv/scripts/activate` для Linux `source venv/bin/activate`
3. Установить зависимости из файла requirements.txt, `pip install -r requirements.txt`
4. Запустить скрипт `python app.py`.

## Пример запроса
```
curl -X POST http://127.0.0.1:5000/get_form \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "param1=value1&param2=21-21-2121"
    /
```

## Пример ответа
```
{
  "param1": "text",
  "param2": "date"
}
```
