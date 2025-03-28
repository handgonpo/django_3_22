from django.contrib import admin
from .models import TodoList

@admin.register(TodoList) # TodoList 모델을 Django Admin에 등록
class TodoListAdmin(admin.ModelAdmin):
    # 목록 페이지에서 보여줄 필드를 설정
    list_display = ('id','name','description', 'complete', 'exp', 'created_at', 'updated_at')

    # Admin 검색창에서 검색할 수 있는 필드 지정
    search_fields = ('name',)

    # 필터 사이드바에 나타날 필드 지정
    list_filter = ('complete', 'created_at')

    '''
    admin.site.register(): 함수 방식, 조금 더 분리됨	
    @admin.register(): 데코레이터 방식, 좀 더 간결하고 직관적  
    '''