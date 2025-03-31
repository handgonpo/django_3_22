from django.urls import path
from users.views import *
from .apis import SignupAPI, LoginAPI, LogoutAPI, UserListAPI


urlpatterns = [
    # 화면 보여주기
    path('login/', LoginView.as_view(), name='login_page'), #127.0.0.1:8000/users/login/
    path('signup/', SignupView.as_view(), name='signup_page'), #127.0.0.1:8000/users/signup/

    # API 처리
    path('api/signup/', SignupAPI.as_view(), name='signup'),
    path('api/login/', LoginAPI.as_view(), name='login_api'),
    path('api/logout/', LogoutAPI.as_view(), name='logout_api'),
    path('api/users/', UserListAPI.as_view(), name='user-list'),
    
    #127.0.0.1:8000/users/api/logout/
]