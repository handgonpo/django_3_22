from rest_framework import viewsets
from .models import TodoList
from .serializers import TodoListSerializer

# ViewSet
class TodoViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all().order_by('-id') #최신글 우선순위 정렬
    serializer_class = TodoListSerializer

# CRUD 전부 자동 처리!
# 필요하면 permission_classes, filter_backends, pagination_class 등 추가로 붙일 수 있음    