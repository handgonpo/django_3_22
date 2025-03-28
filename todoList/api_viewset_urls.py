from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import TodoViewSet 

router = DefaultRouter()
router.register('todos', TodoViewSet, basename='todo') # 127.0.0.1:8000/api/viewsets/todos/<pk>/
# router.register('', TodoViewSet, basename='todo') # 127.0.0.1:8000/api/viewsets/<pk>/

urlpatterns = [
    path('', include(router.urls)),
]

# URL패턴               HTTP메서드   동작
# /api/viewsets/	    GET	        전체 목록 조회 (list)             127.0.0.1:8000/api/viewsets/todos/
# /api/viewsets/	    POST	    새 항목 생성 (create)             127.0.0.1:8000/api/viewsets/todos/
# /api/viewsets/<pk>/	GET         특정 항목(상세) 조회 (retrieve)   127.0.0.1:8000/api/viewsets/todos/<pk>/
# /api/viewsets/<pk>/	PUT         전체 수정 (update)               127.0.0.1:8000/api/viewsets/todos/<pk>/
# /api/viewsets/<pk>/	PATCH	    부분 수정 (partial_update)       127.0.0.1:8000/api/viewsets/todos/<pk>/
# /api/viewsets/<pk>/	DELETE	    삭제 (destroy)                   127.0.0.1:8000/api/viewsets/todos/<pk>/