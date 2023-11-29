# YaCut
Проект YaCut — сервис укорачивания ссылок.

# Возможности сервиса
- Генерация коротких ссылок и связь их с исходными длинными ссылками
- Переадресация на исходный адрес при обращении к коротким ссылкам
Доступны web и api интерфейсы.

# Технологии
- Python 
- Flask  
- SQLAlchemy 

# Установка
## Склонируйте репозиторий:
git clone git@github.com:AbbadonAA/yacut.git
## Активируйте venv и установите зависимости:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
## Создайте в корневой директории файл .env со следующим наполнением:
FLASK_APP=yacut
FLASK_ENV=development или production
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=<ваш_секретный_ключ>

# Управление:
## Для локального запуска выполните команду:

flask run
##  Сервис будет запущен и доступен по следующим адресам:

http://localhost/ - главная страница сервиса;

Если не заполнить поле для короткой ссылки, она будет сгенерирована автоматически.
Короткая ссылка должна быть не длиннее 16 символов (цифры и латинские буквы в любом регистре).
http://localhost/api/id/ - эндпоинт, принимающий POST-запросы;

Схема POST-запроса:
{
"url": "string",
"custom_id": "string" * (необязательное поле)
}
Схема ответа на POST-запрос:
{
"url": "string",
"short_link": "string"
}
http://localhost/api/id/short_id/ - эндпоинт, принимающий GET-запросы.

В адресе вместо <short_id> должна быть указана введённая или сгенерированная короткая ссылка.

Схема ответа на GET-запрос:
{
"url": "string"
}
Полная спецификация API доступна в репозитории - файл openapi.yml

Лицензия
MIT License
Автор
Pushkarev Anton

pushkarevantona@gmail.com
