<<<<<<< HEAD
# API для социальная сети для блоггеров YaTube

### Описание
API для социальной сети для блоггеров на базе Django REST Framework.
Проект API позволяет делать запросы к базе данных социальной сети YaTube. 
Поддерживаются все функции, которые есть в социальной сети (регистрация, получение списка постов и отдельного поста, отправка поста и комментария, подписка на авторов), также реализована авторизация по JWT-токенам при помощи библиотеки Djoser.

### О проекте
Проект базируется на следующих технологиях:
1. Python 3.7.9
2. Django 2.2.6
3. Django REST Framework 2.2.6
4. Djoser + SimpleJWT
5. Виртуальная среда VENV (для разработки проекта в отдельном окружении)
6. Git (GitHub) (для сохранения и отслеживания изменений кода)
7. Линтер Flake8 (для проверки соответствия кода стандарту PEP8)

### Установка и запуск проекта:
1. Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/SvetlanaLogvinova88/API_yatube.git
```
```
cd api_yatube
```

2. Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
```
```
source venv/bin/activate
```

3. Обновить pip в виртуальном окружении:
```
python3 -m pip install --upgrade pip
```

4. Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```

5. Перейти в папку проекта:
```
cd yatube_api
```

6. Выполнить миграции:
```
python3 manage.py migrate
```

7. Запустить проект:
```
python3 manage.py runserver
```

### Примеры запросов:

Получение списка публикаций:
GET http://127.0.0.1:8000/api/v1/posts/

Создание публикации POST:
http://127.0.0.1:8000/api/v1/posts/

Получение списка комментариев к публикации:
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
=======
Описание:
Проект API позволяет делать запросы к базе данных блога YaTube.


Установка:
1. Клонировать репозиторий и перейти в него в командной строке:
https://github.com/SvetlanaLogvinova88/api_final_yatube.git
cd api_final_yatube

2. Cоздать и активировать виртуальное окружение:
python3 -m venv venv
source venv/bin/activate

3. Установить зависимости из файла requirements.txt:
pip install -r requirements.txt

4. Выполнить миграции:
python3 manage.py migrate

5. Запустить проект:
python3 manage.py runserver


Примеры запросов:

Получение списка публикаций GET http://127.0.0.1:8000/api/v1/posts/

Создание публикации POST http://127.0.0.1:8000/api/v1/posts/

Получение списка комментариев к публикации http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
>>>>>>> e67187d638c27dbc06e3296eee7c3071e603a828
