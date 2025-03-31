from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import TodoList
from django.contrib.auth.mixins import LoginRequiredMixin


def todo_Main(request):
    return render(request, "base.html")
# 127.0.0.1:8000/base/ 프로젝트 진입점


def todo_List(request):
    todos = TodoList.objects.all()
    return render(request, "todoList/list.html", {"todos" : todos})
    # render(request, template_name, context=None, content_type=None, status=None, using=None)
    # urls.py에서 "list/" 경로로 연결. 실제 데이터를 context로 전달함
    ''''
    request: 클라이언트로부터 받은 요청 객체
    "todoList/todo_List.html": 렌더링할 템플릿의 경로
    {"todos": todos}: 템플릿에 전달할 context (딕셔너리 형태)
    즉, “요청 → 템플릿 경로 → 전달할 데이터(context)”
    '''


class TodoCreateView(View):

    def get(self, request):
        return render(request, "todoList/create.html")
# urls.py에서 "create/" 경로
# 이후 post()로 실제 저장 로직 추가 가능
    

class TodoDetailView(View):

    def get(self, request, pk):
        return render(request, "todoList/detail.html")
# urls.py에 "detail/<int:pk>/" 경로, context에 실제 todo 객체 전달   


class TodoUpdateView(View):
    def get(self, request, pk):
        todo = get_object_or_404(TodoList, pk=pk)
        return render(request, "todoList/update.html", {"todo": todo})
# "update/<int:pk>/"로 연결됨 → 뷰 템플릿만 렌더링 중 (**수정대상**)       