# Instagram Sync API

Django REST API для:
1. синхронизации постов из Instagram
2.  сохранения данных в PostgreSQL
3.  отправки комментариев через Instagram Graph API

## Запуск через Docker 

### 1. Создать файл `.env` в корне проекта

``` bash
SECRET_KEY=your_django_secret_key
DATABASE_NAME=instagram_db
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
DATABASE_HOST=db
DATABASE_PORT=5432
INSTAGRAM_ACCESS_TOKEN=your_instagram_token
```

### 2. Собрать и запустить контейнер

``` bash
docker-compose up --build
```

Приложение будет доступно по адресу:

http://127.0.0.1:8000/

## Важно

Если вы находитесь в России, Все запросы нужно делать через ВПН
