from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import TodoList

class TodoListSerializer(ModelSerializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    complete = serializers.BooleanField(required=True)
    exp = serializers.IntegerField(required=True)
    
    '''
    항목	                설명
    required=True 명시	  : 명시적으로 필수 필드 설정 가능 (보통 POST 시 유효성 검사 강화 목적)
    PATCH에서는 생략 가능  : partial=True로 들어올 경우 일부 필드만 검사함
    권장 상황	           :  커스터마이징이나 유효성 검사 메시지 커스터마이징할 때 사용
    '''

    class Meta:
        model = TodoList
        fields = '__all__'


    def validate_exp(self, value):
        if value < 0:
            raise serializers.ValidationError("경험치는 0 이상이어야 합니다.")
        return value

""" PUT과 PATCH의 차이점
from rest_framework import serializers
from .models import TodoList

class TodoListSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    complete = serializers.BooleanField(required=True)
    exp = serializers.IntegerField(required=True)

    class Meta:
        model = TodoList
        fields = '__all__' 
"""


""" 
TodoListSerializer는 TodoList 모델과 연결된 serializer이다.
ModelSerializer를 상속하면, model의 필드를 자동으로 분석해서 JSON 변환 구조를 자동 생성해준다.
fields = '__all__' 덕분에 모델의 모든 필드를 자동으로 포함해준다. 
"""