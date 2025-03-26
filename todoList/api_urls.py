# todoList/api_urls.py
from django.urls import path
from .apis import TodoListAPI

urlpatterns = [
    path('todos/', TodoListAPI.as_view(), name='todos'),
]
