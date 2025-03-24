from django.shortcuts import render
from .models import TodoList


def todo_List(request):
    todos = TodoList.objects.all()
    return render(request, "todoList/todo_List.html", {"todos" : todos})
    #render(request, template_name, context=None, content_type=None, status=None, using=None)
''''
request: 클라이언트로부터 받은 요청 객체
"todoList/todo_List.html": 렌더링할 템플릿의 경로
{"todos": todos}: 템플릿에 전달할 context (딕셔너리 형태)
즉, “요청 → 템플릿 경로 → 전달할 데이터(context)”
'''
