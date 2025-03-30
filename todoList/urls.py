from django.urls import path, include
from .views import *

# 127.0.0.1:8000/todoList/제목검색어
urlpatterns = [
   path("update/<int:pk>/", TodoUpdateView.as_view()), # 127.0.0.1:8000/todoList/update/<int:pk>
   path('list/', todo_List, name = 'todo_List'), # 127.0.0.1:8000/todoList/list/ 경로변경
   path("create/", TodoCreateView.as_view()),# 127.0.0.1:8000/todoList/create/
   path("detail/<int:pk>/", TodoDetailView.as_view()), # 127.0.0.1:8000/todoList/detail/<str:name>/ name = 공부를 찾아서 리턴 
   path("<int:pk>/", TodoDetailView.as_view()), # 127.0.0.1:8000/todoList/<int:pk>/
 ]  

# urls.py (라우팅) -> views.py(로직) -> ~~.html(템플릿)