#from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TodoList
from .serializers import TodoListSerializer

class TodoListAPI(APIView):

    def get(self, request):
        todos = TodoList.objects.all().order_by("-created_at")
        serializer = TodoListSerializer(todos, many=True)
        return Response(serializer.data)
    

""" class TodoCreateAPI(APIView):

    def post(self, request):
        serializer = TodoListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        return Response(TodoListSerializer(todo).data, status=status.HTTP_201_CREATED)    
    

class TodoRetrieveAPI(APIView):

    def get(self, request, pk):
        try:
            todo = TodoList.objects.get(pk=pk)
        except TodoList.DoesNotExist:
            return Response({"error":"해당하는 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        serializer = TodoListSerializer(todo)
        return Response(serializer.data)
    

class TodoUpdateAPI(APIView):

    def put(self, request, pk):
        try:
            todo = TodoList.objects.get(pk=pk)
        except TodoList.DoesNotExist:
            return Response({"error":"해당하는 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        serializer = TodoListSerializer(todo, data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        serializer = TodoListSerializer(todo)
        return Response(serializer.data)

    def patch(self, request, pk):
        try:
            todo = TodoList.objects.get(pk=pk)
        except TodoList.DoesNotExist:
            return Response({"error":"해당하는 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        serializer = TodoListSerializer(todo, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        serializer = TodoListSerializer(todo)
        return Response(serializer.data)
    

class TodoDeleteAPI(APIView):

    def delete(self, request, pk):
        try:
            todo = TodoList.objects.get(pk=pk)
        except TodoList.DoesNotExist:
            return Response({"error":"해당하는 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 """

""" class TodoListAPI(APIView):

    # GET 요청: 전체 할 일 목록 조회: DB에 있는 모든 TodoList 객체를 가져와서 JSON으로 변환
    def get(self, request):
        todos = TodoList.objects.all()
        serializer = TodoListSerializer(todos, many=True)
        return Response(serializer.data)

    # POST 요청: 새로운 할 일 생성: 클라이언트가 보낸 JSON 데이터를 DB에 저장 
    def post(self, request):
        serializer = TodoListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # DB에 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
"""