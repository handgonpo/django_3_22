from rest_framework.serializers import ModelSerializer
from .models import TodoList

class TodoListSerializer(ModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'

""" 
TodoListSerializer는 TodoList 모델과 연결된 serializer이다.
ModelSerializer를 상속하면, model의 필드를 자동으로 분석해서 JSON 변환 구조를 자동 생성해준다.
fields = '__all__' 덕분에 모델의 모든 필드를 자동으로 포함해준다. 
"""