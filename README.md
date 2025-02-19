## Установка и настройка:

### 1. Создание файла окружения 
Создайте файл `.env` в папке `electronic_journal` с следующими данными.  
Пример данных:  
DB_USER=postgres  
DB_PASSWORD=4342  
DB_HOST=db  
DB_PORT=5432  
DB_NAME=electronic_journal

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
