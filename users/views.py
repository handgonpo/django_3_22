from django.shortcuts import render
from django.views import View


class LoginView(View):
    def get(self, request):
        return render(request, "users/login.html")


class SignupView(View):
    def get(self, request):
        return render(request, "users/signup.html")


'''
views.py → 프론트엔드 렌더링용 뷰
(예: 로그인 화면 HTML, 회원가입 화면 HTML 보여주기)

'''