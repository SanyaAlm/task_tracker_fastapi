## Установка и настройка:

### 1. Создание файла окружения 
Создайте файл `.env` в папке `electronic_journal` с следующими данными.  
Пример данных:  
POSTGRES_HOST=db

POSTGRES_PORT=5432

POSTGRES_USER=postgres

POSTGRES_PASSWORD=4342

POSTGRES_DB=scheduler


### 2. Установка зависимостей:

Для установки зависимостей используйте [Poetry](https://python-poetry.org/). Выполните следующую команду:

```bash
poetry install
```
### 3. Запуск Docker контейнеров:
Для поднятия Docker контейнеров выполните команду:
```bash
docker compose up -d --build
```
### 4. Доступ к API
API эндпоинты будут доступны по адресу: (http://localhost:8001/docs)
