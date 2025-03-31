from django.contrib import admin
from django.urls import path, include
from todoList import views

urlpatterns = [
    path('admin/', admin.site.urls), # 127.0.0.1:8000/admin/
    path('', views.todo_Main, name = 'base'), # 127.0.0.1:8000/base.html
    path('todoList/', include('todoList.urls')), # 127.0.0.1:8000/todoList/ -> 장고 탬플릿 기반
    path("users/", include("users.urls")), # 127.0.0.1:8000/users/
    path('api/', include('todoList.api_urls')), # 127.0.0.1:8000/api/ 
    # -> DRF 기반으로 todoList>api_urls.py에 정의된 모든 URL 앞에 접두어 처럼 api/를 붙여서 최종 URL을 만든다는 뜻
    path("api/viewsets/", include("todoList.api_viewset_urls")), # 127.0.0.1:8000/api/viewsets/<int:pk>/
]

'''
1. 127.0.0.1:8000/admin/
2. 127.0.0.1:8000/base/ 
 - config>urls.py -> todoList>views.py -> base.html
 - base.html(head.html,header.html,footer.html), content(list.html, detail.html, create.html, update.html)
3. 127.0.0.1:8000/todoList/list/
 - config>urls.py -> todoList>urls.py -> todoList>views.py -> def todo_List
4. 127.0.0.1:8000/users/
5. 127.0.0.1:8000/api/
6. 127.0.0.1:8000/api/viewsets/<int:pk>/

-문제점
1. 로그인후 메인으로 가면 리스트를 볼수가 없다. 해결)처음 로그인 할때는 목록보기가 없지만 로그인후 메인으로 갈때는 목록보기를 만들어준다.
2. 로그아웃을 안하고 서버를 종료한 후 다시 서버 실행시 로그아웃이 안되어 있고 로그인 상태이다.
'''
