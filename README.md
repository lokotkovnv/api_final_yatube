# api_final
Блог yatube разработанный при помощи django rest framework
В блоге реализованы функции написания постов, комментариев и подписок пользователей друг на друга
Все функции производятся путем запросов к эндпойнтам проекта
Для локального запуска проекта необходимо развернуть виртуальное окружение, установить зависимости, выполнить миграции и запустить проект командой python manage.py runserver
примеры запросов и ответов:
GET http://127.0.0.1:8000/api/v1/posts - получение списка публикаций

Ответ:
{
"count": 123,
"next": "http://api.example.org/accounts/?offset=400&limit=100",
"previous": "http://api.example.org/accounts/?offset=200&limit=100",
"results": [
{}
]
}


GET http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/ - получение комментария к публикации по id

Ответ:
{
"id": 0,
"author": "string",
"text": "string",
"created": "2019-08-24T14:15:22Z",
"post": 0
}
