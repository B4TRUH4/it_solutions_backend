# IT-Solutions API

## Описание проекта

Проект представляет собой API для получения/изменения данных об объявлениях по ссылке https://www.farpost.ru/vladivostok/service/construction/guard/+/Системы+видеонаблюдения/

## Технологии

- **Python 3.10**
- **Django 5.0.1**
- **Django REST framework**
- **PostgreSQL**
- **Docker**
- **Nginx**
- **Gunicorn**

## Установка и настройка

### Требования

- Docker и Docker Compose

### Шаги установки

1. **Клонируйте репозиторий:**

    ```bash
    git clone https://github.com/B4TRUH4/it_solutions_backend
    cd it_solutions_backend
    ```

2. **Настройте файл окружения `.env`:**

    Создайте файл `.env` в корне проекта и добавьте следующие переменные (замените значения на собственные):

    ```env
    DATABASE_URL=postgres://postgres:postgres@db:5432/postgres
    POSTGRES_DB=postgres
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    SECRET_KEY=secret_key
    ```
   
3. **Выберите версию проекта:**
   - для запуска dev-версии выполните:
    ```bash
    docker compose up --build
    ```
   - для запуска prod-версии выполните:
    ```bash
    docker compose -f docker-compose.prod.yaml up
    ```

4. **Примените миграции (если не применились автоматически):**

    ```bash
    docker-compose exec server python manage.py makemigrations
    docker-compose exec server python manage.py migrate
    ```
5. **Заполните базу данных данными:**

   Так как на сайте farpost есть капча, данные были добавлены вручную в файл `server/default_data/farpost_advert.json`

   ```json
   [
     {
       "id": 109787028,
       "title": "Установка видеонаблюдения и домофонии",
       "author": "Primtec",
       "views": 723,
       "position": 1
     },
     ...
   ]
   ```
   
   Была создана команда для заполнения базы данных этими данными. Выполняется следующим образом:

    ```bash
    docker-compose exec server python manage.py load_adverts "путь_к_файлу"
    ```
   В случае использования данного файла:
   ```bash
    docker-compose exec server python manage.py load_adverts default_data/farpost_advert.json
    ```
   Можно было использовать Selenium и проходить ее вручную при запросе, но данных было не так много)))


## API

Серверная часть предоставляет REST API для взаимодействия с клиентской частью. Основные эндпоинты включают:

- `/api/adverts/` - управление объявлениями
- `/api/auth/` - управление пользователями и аутентификация

Присутствует возможность создания пользователя (`api/auth/users/`), а также авторизация через JWT-токены
(`api/auth/jwt/...`)

Для доступа к объявлениям необходимо выполнить следующие действия:

1. **Создать аккаунт (POST запрос на `api/auth/users/`)**
2. **Получить access и refresh токены (`api/auth/jwt/create/`)**
3. **При запросах передавать в заголовке `Authorization: Bearer {access-токен}`**
4. **При окончании действия access-токена обновить его (POST запрос на `api/auth/jwt/refresh/` c указанием в теле refresh-токена)

Более подробно и вместе с примерами запросов эндпоинты можно изучить по пути `/api/schema/swagger-ui/`.
