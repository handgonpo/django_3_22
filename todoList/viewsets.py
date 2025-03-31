from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import TodoList
from .serializers import TodoListSerializer

# ViewSet
class TodoViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all().order_by('-id') #최신글 우선순위 정렬
    serializer_class = TodoListSerializer
    permission_classes = [IsAuthenticated]  # 로그인한 사용자만 접근 가능
    # 필터링, 검색, 정렬 기능
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']   # ?search=공부
    ordering_fields = ['exp', 'completed_at'] # ?ordering=exp

'''
항목	          :   설명
queryset	      :  TodoList 모델의 모든 객체를 id 역순으로 정렬
serializer_class  :  데이터를 직렬화/역직렬화할 TodoListSerializer 지정
ModelViewSet	  :  list, retrieve, create, update, partial_update, destroy 모두 자동 생성
'''

# CRUD 전부 자동 처리!
# 필요하면 permission_classes, filter_backends, pagination_class 등 추가로 붙일 수 있음    