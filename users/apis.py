from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model
User = get_user_model()  # ✅ 커스텀 유저 모델을 사용할 수 있게 설정



# 회원가입 API
class SignupAPI(APIView):
    permission_classes = [AllowAny]  # 누구나 접근 가능

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        # 사용자 이름 중복 확인
        if User.objects.filter(username=username).exists():
            return Response({"message": "이미 존재하는 사용자입니다."}, status=status.HTTP_400_BAD_REQUEST)

        # 사용자 생성 (비밀번호는 자동 암호화됨)
        User.objects.create_user(username=username, password=password)
        return Response({"message": "회원가입이 완료되었습니다."}, status=status.HTTP_201_CREATED)


# 로그인 API
class LoginAPI(APIView):
    permission_classes = [AllowAny]  # 누구나 접근 가능

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        # 사용자 인증
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)  # 세션 로그인 처리
            return Response({"message": "로그인 성공"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "아이디 또는 비밀번호가 틀렸습니다."}, status=status.HTTP_401_UNAUTHORIZED)


# 로그아웃 API
class LogoutAPI(APIView):
    permission_classes = [IsAuthenticated]  # 로그인한 사용자만 접근 가능

    def post(self, request):
        logout(request)  # 세션 로그아웃 처리
        return Response({"message": "로그아웃 되었습니다."}, status=status.HTTP_200_OK)


# 로그인한 사용자만 볼 수 있는 사용자 목록 API
class UserListAPI(APIView):
    permission_classes = [IsAuthenticated]  # 로그인한 사용자만 접근 가능

    def get(self, request):
        users = User.objects.all().values("id", "username")  # 전체 사용자 조회
        return Response({"users": list(users)}, status=status.HTTP_200_OK)
