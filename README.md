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
