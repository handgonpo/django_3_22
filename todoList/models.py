from django.db import models

class TodoList(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    complete = models.BooleanField(default=False)
    exp = models.PositiveIntegerField(default=0)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name  
    # admin 페이지에서 TodoList 객체를(제목) 보기 쉽게 표시하기 위해 __str__ 메서드를 정의