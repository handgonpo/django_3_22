from django.urls import path, include
from .views import *

# 127.0.0.1:8000/todoList/제목검색어
urlpatterns = [
   path('', todo_List, name = 'todo_List'), # 127.0.0.1:8000/todoList/ 경로변경
   path("create/", TodoCreateView.as_view()),# 127.0.0.1:8000/todoList/create/
   path("<str:name>/", todo_detail), # 127.0.0.1:8000/todoList/<str:name>/ name = 공부를 찾아서 리턴 
]

# urls.py (라우팅) -> views.py(로직) -> ~~.html(템플릿)