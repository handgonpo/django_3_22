from django.urls import path
from .views import todo_Main, todo_List, TodoCreateView, TodoDetailView, TodoUpdateView

# 127.0.0.1:8000/todoList/제목검색어
urlpatterns = [
   path('list/', todo_List, name = 'todo_List'), # 목록조회 127.0.0.1:8000/todoList/list/ 
   path("create/", TodoCreateView.as_view()),# 생성 127.0.0.1:8000/todoList/create/
   path("detail/<int:pk>/", TodoDetailView.as_view()), # 상세보기 127.0.0.1:8000/todoList/detail/<int:pk>/   
   path("update/<int:pk>/", TodoUpdateView.as_view()), # 수정 127.0.0.1:8000/todoList/update/<int:pk> 
 ]  

# urls.py (라우팅) -> views.py(로직) -> ~~.html(템플릿)

'''
변경	                       :  이유
get_object_or_404 사용	     :  pk로 객체 불러올 때 예외 처리 간편하게
클래스 뷰에서 context 전달	  :  템플릿에서 실제 데이터 사용할 수 있도록
todo_detail 함수형 뷰 제거	  :  URL 매핑 없음 + 기능 중복
TodoListView 제거	           :  사용되지 않음
urls.py 이름 지정 (name=...) :	템플릿에서 {% url %}로 쉽게 호출 가능
'''