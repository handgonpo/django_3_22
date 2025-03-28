# todoList/api_urls.py
from django.urls import path, include
from .apis import *

urlpatterns = [
    # APIView
    path('todos/', TodoListAPI.as_view(), name='todos'), # 127.0.0.1:8000/api/todos
    path('create/', TodoCreateAPI.as_view(), name='create'), # 127.0.0.1:8000/api/create
    path('retrieve/<int:pk>/', TodoRetrieveAPI.as_view(), name='retrieve'), # 127.0.0.1:8000/api/retrieve
    path('update/<int:pk>/', TodoUpdateAPI.as_view(), name='update'), # 127.0.0.1:8000/api/update
    path('delete/<int:pk>/', TodoDeleteAPI.as_view(), name='delete'), # 127.0.0.1:8000/api/delete
    # generics.APIView
    path("generics/list/", TodoGenericsListAPI.as_view()), # 127.0.0.1:8000/api/generics/list/
    path("generics/retrieve/<int:pk>/", TodoGenericsRetrieveAPI.as_view()), # 127.0.0.1:8000/api/generics/retrieve/1/
    path("generics/create/", TodoGenericsCreateAPI.as_view()), # 127.0.0.1:8000/api/generics/create/
    path("generics/update/<int:pk>/", TodoGenericsUpdateAPI.as_view()), # 127.0.0.1:8000/api/generics/update/1/
    path("generics/delete/<int:pk>/", TodoGenericsDeleteAPI.as_view()), # 127.0.0.1:8000/api/generics/delete/1/
    # Add generics
    path("generics/", TodoGenericsListCreateAPI.as_view()), # 127.0.0.1:8000/api/generics/
    path("generics/<int:pk>/", TodoGenericsRetrieveUpdateDeleteAPI.as_view()), # 127.0.0.1:8000/api/generics/1/  
]
