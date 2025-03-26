from django.contrib import admin
from django.urls import path, include
from todoList import views

urlpatterns = [
    path('admin/', admin.site.urls), # 127.0.0.1:8000/admin/
    path('', views.todo_Main, name = 'todo_Main'), # 127.0.0.1:8000/todo_Main.html
    path('todoList/', include('todoList.urls')), # 127.0.0.1:8000/todoList/ -> 장고 탬플릿 기반
    path('api/', include('todoList.api_urls')), # 127.0.0.1:8000/api/ 
    # -> DRF 기반으로 todoList>api_urls.py에 정의된 모든 URL 앞에 접두어 처럼 api/를 붙여서 최종 URL을 만든다는 뜻
]
