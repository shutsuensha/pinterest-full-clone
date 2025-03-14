tags_metadata = [
    {
        "name": "users",
        "description": "👤 **Пользователи**:\n"
        "- 🔹 Регистрация\n"
        "- 🔹 Верификация почты\n"
        "- 🔹 Сброс пароля\n"
        "- 🔹 JWT-аутентификация\n"
        "- 🔹 Отзыв JWT-токена\n"
        "- 🔹 Получение пользователя\n"
        "- 🔹 Загрузка/изменение изображения\n"
        "- 🔹 Загрузка/изменение баннера\n"
        "- 🔹 Обновление информации",
    },
    {
        "name": "pins",
        "description": "📌 **Пины**:\n"
        "- 🔹 Получение списка\n"
        "- 🔹 Создание\n"
        "- 🔹 Удаление\n"
        "- 🔹 Поиск по тегам\n"
        "- 🔹 Загрузка изображения/видео\n"
        "- 🔹 Получение отдельного пина\n"
        "- 🔹 Получение всех пинов пользователя\n"
        "- 🔹 Сохранение и удаление пинов\n"
        "- 🔹 Получение списка лайкнутых пинов",
    },
    {
        "name": "tags",
        "description": "🏷 **Теги**:\n"
        "- 🔹 Получение всех тегов\n"
        "- 🔹 Создание тега\n"
        "- 🔹 Получение пинов по тегу\n"
        "- 🔹 Получение тегов на пине",
    },
    {
        "name": "comments",
        "description": "💬 **Комментарии**:\n"
        "- 🔹 Создание комментариев\n"
        "- 🔹 Получение списка\n"
        "- 🔹 Подсчет количества комментариев\n"
        "- 🔹 Загрузка изображений/видео\n"
        "- 🔹 Создание ответов на комментарии\n"
        "- 🔹 Получение всех ответов на комментарии",
    },
    {
        "name": "likes",
        "description": "❤️ **Лайки**:\n"
        "- 🔹 Лайки на пинах/комментариях\n"
        "- 🔹 Удаление лайков\n"
        "- 🔹 Проверка наличия лайка\n"
        "- 🔹 Подсчет количества лайков",
    },
    {
        "name": "subscriptions",
        "description": "🔔 **Подписки**:\n"
        "- 🔹 Подписка/отписка от пользователя\n"
        "- 🔹 Проверка подписки\n"
        "- 🔹 Получение списка подписчиков\n"
        "- 🔹 Получение списка подписок\n"
        "- 🔹 Подсчет количества подписчиков/подписок",
    },
    {
        "name": "chats",
        "description": "💬 **Чаты**:\n" "- 🔹 Изменение цвета/размера/открытости чата",
    },
    {
        "name": "messages",
        "description": "📩 **Сообщения**:\n"
        "- 🔹 Создание сообщений\n"
        "- 🔹 История сообщений\n"
        "- 🔹 Последнее сообщение\n"
        "- 🔹 Проверка существования чатов\n"
        "- 🔹 Создание изображений/видео в сообщениях\n"
        "- 🔹 Подсчет непрочитанных сообщений",
    },
    {
        "name": "notauth",
        "description": "🏠 **Главная страница**:\n"
        "- 🔹 Получение изображений для неавторизованных пользователей",
    },
    {"name": "health", "description": "⚙ **Статус API**:\n" "- 🔹 Проверка работоспособности API"},
    {
        "name": "pins-cache",
        "description": "🗄 **Кэширование пинов (пример)**:\n"
        "- 🔹 Получение списка пинов с кэшем\n"
        "- 🔹 Очистка кэша при удалении/создании пина",
    },
    {
        "name": "users-google-auth",
        "description": "🔑 **Google OAuth2 (пример)**:\n"
        "- 🔹 Аутентификация через Google\n"
        "- 🔹 Получение данных авторизованного пользователя",
    },
    {
        "name": "users-httpx",
        "description": "🔗 **HTTPX Users (пример)**:\n" "- 🔹 CRUD-операции через HTTPX",
    },
    {
        "name": "users-mysql",
        "description": "🛢 **MySQL Users (пример)**:\n"
        "- 🔹 CRUD-операции через PostgreSQL + Aiomysql",
    },
    {
        "name": "users-mongodb",
        "description": "📦 **MongoDB Users (пример)**:\n"
        "- 🔹 CRUD-операции через MongoDB (async)",
    },
    {
        "name": "users-celery",
        "description": "📤 **Celery (пример)**:\n"
        "- 🔹 Загрузка медиа через Celery-воркер\n"
        "- 🔹 Проверка статуса задачи",
    },
    {
        "name": "sse",
        "description": "📺 **Server-Sent Events (пример)**:\n" "- 🔹 Потоковая передача видео",
    },
    {
        "name": "yandex-s3",
        "description": "☁ **Yandex S3 (пример)**:\n"
        "- 🔹 Загрузка медиа в Yandex Bucket\n"
        "- 🔹 Получение файлов из хранилища",
    },
    {
        "name": "graphql",
        "description": "🔗 **GraphQL (пример)**:\n" "- 🔹 GraphQL API и документация",
    },
]

description = """
### 🖼️ Описание API
Этот API предназначен для работы с **Pint3rest** – платформой для обмена изображениями, видео и идеями.

#### 🔑 Основной функционал:
- **Пользователи**: регистрация, вход, выход, верификация почты, сброс пароля, JWT-аутентификация (access/refresh tokens), отзыв JWT-токенов, загрузка изображений, обновление профиля, просмотр профилей всех пользователей.
- **Пины**: создание, удаление, сохранение, лайк пина, поиск, загрузка медиа, управление сохранениями, лайками и созданными пинами, просмотр всех пинов, просмотр отдельного пина + related.
- **Теги**: управление тегами, поиск пинов по тегам.
- **Комментарии**: добавление комментариев к пину, ответы на комментарии, загрузка медиа, просмотр комментариев на пине.
- **Лайки**: лайки для пинов и комментариев.
- **Подписки**: управление подписками, получение списка подписчиков и подписок.
- **Чаты и сообщения**: просмотр чатов, просмотр истории чата, отправка сообщений.

#### 🛠️ Используемые технологии:
- **FastAPI** – REST и GraphQL API.
- **FastAPI-Cache** – для кэширования на уровне API.
- **FastAPI-Mail** – для отправки email через FastAPI.
- **SQLAlchemy** – ORM для работы с базами данных.
- **Pydantic** – для валидации запросов/ответов и **pydantic-settings** – для управления переменными окружения.
- **JWT** – access/refresh tokens, revoke tokens.
- **OAuth2** – Google Auth.
- **PostgreSQL, MySQL, MongoDB** – для работы с реляционными и нереляционными базами данных.
- **Redis** – для кэширования данных, отзыва токенов, работы брокера и получения результатов Celery, а также для Celery RedBeat.
- **Celery** – для отправки писем верификации/сброса пароля, обработки изображений (сохранение, изменение размера, обновление базы данных).
- **Celery Beat** – для отправки рекламы на почту.
- **Docker** – для контейнеризации приложений.
- **Docker Compose** – для управления многоконтейнерными приложениями.
- **Nginx** – для проксирования запросов `/api`, `/ws` и обеспечения безопасности.
- **SSL** – для безопасного соединения через HTTPS.
- **VPS** – для размещения приложения на виртуальном сервере.
- **Yandex S3** – для хранения и получения файлов (Yandex bucket).
- **httpx** – для взаимодействия с внешними API.
- **Websockets** – реализация чатов с использованием FastAPI.websockets.
- **SSE (Server-Sent Events)** – для получения уведомлений от сервера на клиенте в режиме реального времени.
- **Asyncio** – для асинхронного программирования.
- **Aiofiles** – для асинхронной работы с файловой системой.
- **Logging** – для ведения логов в приложении.
- **Pytest** – для тестирования и обеспечения качества кода.
- **Ruff** – линтинг и форматирование.
- **Alembic** – для миграций базы данных.
- **GitLab CI/CD** – для настройки CI/CD Pipeline (build, lint/format, migrations, test, deploy).
- **GraphQL (Strawberry)** – для построения GraphQL API.



#### 📝 Автор
- 🐰 **Daniil Kupryianchyk**

#### 📬 Контакты:
- 📧 **Email**: [dankupr21@gmail.com](mailto:dankupr21@gmail.com)
- 💬 **Telegram**: [@evalshine](https://t.me/evalshine)
- 🐙 **GitHub**: [shutsuensha](https://github.com/shutsuensha)

#### 🔗 Полезные ссылки:
- 🚀 **GraphQL API**: [`pint3rest.xyz/api/graphql`](https://pint3rest.xyz/api/graphql)
- 📜 **Документация (Swagger UI)**: [`pint3rest.xyz/api/docs`](https://pint3rest.xyz/api/docs)
- 🌐 **Главная страница**: [`pint3rest.xyz`](https://pint3rest.xyz)
"""

title = "Pint3rest API"
version = "1.0.0"

license_info = {
    "name": "MIT",
    "url": "https://opensource.org/licenses/MIT",
}
