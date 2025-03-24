from django.shortcuts import render
from .models import TodoList


def todo_List(request):
    todos = TodoList.objects.all()
    return render(request, "todoList/todo_List.html", {"todos" : todos})
