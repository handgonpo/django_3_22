from django.db import models
from django.utils import timezone

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

    def save(self, *args, **kwargs):
        if self.complete and self.completed_at is None:
            self.completed_at = timezone.now()
        if not self.complete and self.completed_at is not None:
            self.completed_at = None
        super().save(*args, **kwargs)