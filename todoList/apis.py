from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TodoList
from .serializers import TodoListSerializer

# 1. 기능: 전체 TodoList 항목을 불러와 최신 순으로 정렬 후 JSON 응답
class TodoListAPI(APIView): # 클라이언트 요청으로 API를 통해 데이터 전체 목록을 JSON 형식으로 직렬화하여 응답하는 과정

    def get(self, request):
        todos = TodoList.objects.all().order_by("-created_at")
        serializer = TodoListSerializer(todos, many=True)
        return Response(serializer.data)
'''
✅ 1. TodoListAPI – 할 일 전체 목록 보기
클라이언트(사용자)가 서버에게 "지금까지 저장된 모든 할 일 목록을 보여줘!"라고 요청하면,
서버는 데이터베이스에 있는 할 일들을 꺼내서 보기 좋은 JSON 형식으로 보내주는 기능입니다.
'''   

# 2. 기능: 새 TodoList 항목을 생성하고 결과 반환
class TodoCreateAPI(APIView): # 클라이언트가 전송한 JSON 데이터를 바탕으로 새로운 Todo 항목을 생성하고, 생성된 객체를 JSON 형식으로 응답하는 과정

    def post(self, request):
        serializer = TodoListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        return Response(TodoListSerializer(todo).data, status=status.HTTP_201_CREATED)
'''
✅ 2. TodoCreateAPI – 새로운 할 일 추가하기
사용자가 "이런 할 일을 새로 만들고 싶어요!" 하고 내용을 서버에 보내면,
서버는 그 내용을 저장하고, 새로 만들어진 할 일 정보를 다시 JSON으로 보내주는 기능입니다.
'''

# 3. 기능: 특정 pk를 가진 단일 TodoList 항목 반환
class TodoRetrieveAPI(APIView): # 클라이언트가 특정 ID로 요청한 데이터를 조회하여, 해당 Todo 항목을 JSON 형식으로 응답하는 과정

    def get(self, request, pk):
        try:
            todo = TodoList.objects.get(pk=pk)
        except TodoList.DoesNotExist:
            return Response({"error":"해당하는 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        serializer = TodoListSerializer(todo)
        return Response(serializer.data)
'''
✅ 3. TodoRetrieveAPI – 특정 할 일 하나만 보기
사용자가 "저장된 할 일 중에서 3번 ID에 해당하는 것만 보여줘!"라고 요청하면,
서버는 그 ID에 해당하는 할 일을 찾아서 JSON 형식으로 보내주는 기능입니다.
'''


# 4. 기능: 특정 TodoList 항목의 전체 또는 일부 필드를 수정
class TodoUpdateAPI(APIView): # 클라이언트가 보낸 JSON 데이터를 이용해 특정 Todo 항목을 수정하고, 수정된 결과를 JSON 형식으로 응답하는 과정

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
'''
✅ 4. TodoUpdateAPI – 기존 할 일 수정하기
사용자가 "2번 할 일의 내용을 바꾸고 싶어요!"라고 새로운 내용을 보내면,
서버는 그 할 일을 찾아서 내용을 수정하고, 바뀐 결과를 JSON으로 다시 보내주는 기능입니다.
'''


# 5. 기능: 특정 ID의 TodoList 항목 삭제
class TodoDeleteAPI(APIView): # 클라이언트가 요청한 특정 Todo 항목을 데이터베이스에서 삭제하고, 성공 여부를 응답하는 과정

    def delete(self, request, pk):
        try:
            todo = TodoList.objects.get(pk=pk)
        except TodoList.DoesNotExist:
            return Response({"error":"해당하는 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''
✅ 5. TodoDeleteAPI – 할 일 삭제하기
사용자가 "4번 할 일을 지워주세요!"라고 요청하면,
서버는 해당 번호의 할 일을 삭제하고, 삭제되었다는 응답만 간단히 보내주는 기능입니다.
'''


class TodoGenericsListAPI(generics.ListAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


class TodoGenericsRetrieveAPI(generics.RetrieveAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


class TodoGenericsCreateAPI(generics.CreateAPIView):
    serializer_class = TodoListSerializer


class TodoGenericsUpdateAPI(generics.UpdateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


class TodoGenericsDeleteAPI(generics.DestroyAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


class TodoGenericsListCreateAPI(generics.ListCreateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


class TodoGenericsRetrieveUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
















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
