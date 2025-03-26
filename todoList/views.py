from django.shortcuts import render
from .models import TodoList
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# path("update/<int:pk>/", TodoUpdateView.as_view()), 
# path("create/", TodoCreateView.as_view()),
# path("list/", TodoListView.as_view()), 
# path("<int:pk>/", TodoDetailView.as_view()), 
# path("<str:name>/", todo_detail),  

def todo_Main(request):
    return render(request, "base.html")

def todo_List(request):
    todos = TodoList.objects.all()

    # search = request.GET.get("search")
    # if search:
    #     todos = todos.filter(name__icontains=search)

    return render(request, "todoList/list.html", {"todos" : todos})
    #render(request, template_name, context=None, content_type=None, status=None, using=None)
''''
request: 클라이언트로부터 받은 요청 객체
"todoList/todo_List.html": 렌더링할 템플릿의 경로
{"todos": todos}: 템플릿에 전달할 context (딕셔너리 형태)
즉, “요청 → 템플릿 경로 → 전달할 데이터(context)”
'''

def todo_detail(request, name):
    # todo = Todo.objects.get(pk=pk) == Todo.objects.get(id=pk)
    # try:
    #     todo = Todo.objects.get(id=pk) # -> Todo Object
    # except Todo.DoesNotExist: # 예외처리
    #     return HttpResponse("없는 페이지입니다.", status=404)
    todos = TodoList.objects.filter(name__icontains=name) # name__icontains=name : name 필드에 name이 포함된 객체를 필터링
    if not todos.exists():
        return HttpResponse("없는 페이지입니다.", status=404)
    
    return render(request, "todoList/todo_List.html", {"todos": todos, "keyword": name})


def todo_detail_name(request, name):
    todo = TodoList.objects.filter(name__icontains=name) # queryset
    first = todo.first()
    last =  todo.last()
    return render(request, "todo/todo.html", {"todo": todo, "first": first, "last": last})


class TodoCreateView(View):

    def get(self, request):
        return render(request, "todo/create.html")
    

class TodoListView(LoginRequiredMixin, View):

    def get(self, request):
        # todos = Todo.objects.all()
        return render(request, "todo/list2.html")
    

class TodoDetailView(View):

    def get(self, request, pk):
        return render(request, "todo/detail.html")
    

class TodoUpdateView(View):

    def get(self, request, pk):
        return render(request, "todo/update.html")