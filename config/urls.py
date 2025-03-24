from django.contrib import admin
from django.urls import path, include
from todoList import views

urlpatterns = [
    path('admin/', admin.site.urls), # 127.0.0.1:8000/admin/
    path('', views.todo_Main, name = 'todo_Main'), # 127.0.0.1:8000/
    path('todoList/', include('todoList.urls')), # 127.0.0.1:8000/todoList/
]
