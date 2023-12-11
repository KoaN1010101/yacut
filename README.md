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
```
git clone git@github.com:KoaN1010101/yacut.git
```
## Активируйте venv и установите зависимости:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Создайте в корневой директории файл .env со следующим наполнением:
```
FLASK_APP=yacut
FLASK_ENV=development или production
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=<ваш_секретный_ключ>
```
# Управление:

## Установить alembic и выполнить миграции
```
alembic init --template async alembic 
alembic revision --autogenerate -m "First migrate"
alembic upgrade head
```
## Запустить приложение
```
uvicorn app.main:app --reload
```

}
```
# Автор
Никулин Владимир
