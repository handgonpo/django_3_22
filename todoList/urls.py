from django.urls import path
from todoList import views

urlpatterns = [
    path('', views.todo_List), # 127.0.0.1:8000/todo_List/
]