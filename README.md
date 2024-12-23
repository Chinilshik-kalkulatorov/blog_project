
# Django Blog Project

Этот проект представляет собой базовый блог на Django с функционалом управления статьями и интерфейсом для пользователей.

## Основные возможности:
- Модель `Article` для управления статьями.
- Главная страница с пагинацией и кнопкой «Загрузить ещё».
- Детальная страница для просмотра статьи.
- Тестирование с использованием **pytest** и **pytest-django**.
- Swagger-документация API (drf-yasg).

---

## Как запустить проект

### 1. Склонировать репозиторий:
```bash
git clone https://github.com/Chinilshik-kalkulatorov/blog_project.git
cd blog_project
```

### 2. Создать виртуальное окружение (опционально):
Для Linux/MacOS:
```bash
python3 -m venv venv
source venv/bin/activate
```
Для Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Установить зависимости:
```bash
pip install -r requirements.txt
```
> **Примечание:** Если файл `requirements.txt` отсутствует, создайте его и добавьте:
> - Django
> - Pillow
> - drf-yasg
> - pytest-django

### 4. Выполнить миграции базы данных:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Запустить сервер разработки:
```bash
python manage.py runserver
```
Откройте проект в браузере по адресу: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Структура проекта

```
blog_project/
├── blog/
│   ├── models.py        # Модель Article.
│   ├── views.py         # Вьюхи для списка и деталей.
│   ├── api.py           # DRF API (ArticleViewSet, ArticleListAPI).
│   ├── serializers.py   # Сериализаторы для модели Article.
│   ├── tests.py         # Тесты на базе встроенного unittest.
│   └── templates/blog/  # Шаблоны для HTML (список, детали, частичные).
│
├── static/
│   └── css/styles.css   # Базовые стили.
│
├── config/
│   ├── settings.py      # Настройки проекта.
│   ├── urls.py          # Главный роутер (подключение blog.urls).
│   └── swagger.py       # Swagger-конфигурация (опционально).
│
├── requirements.txt     # Список зависимостей.
└── manage.py            # Главный файл управления.
```

---

## Swagger-документация

### Установка:
Подключите **drf-yasg** в `INSTALLED_APPS` и настройте маршруты в `urls.py`:
```python
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version='v1',
        description="API для управления статьями",
    ),
    public=True,
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
```

Swagger доступен по адресу:
- [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

---

## Запуск тестов

Используем `pytest` и `pytest-django`. Установите пакеты:
```bash
pip install pytest pytest-django
```

Запуск всех тестов:
```bash
pytest
```

---

## Полезные детали

- Настроены пути `MEDIA_URL` и `MEDIA_ROOT` для загрузки изображений.
- `.gitignore` содержит исключения для `venv/`, `__pycache__/`, `db.sqlite3` и других временных файлов.

---
