# 로컬 개발 설정

# 로컬 개발 환경 설정 (base.py를 상속받아 환경별로 override)
from .base import *
import os, environ
from pathlib import Path

# 환경변수 로딩 설정 (.env 파일을 기반으로 환경별 변수 읽어오기)
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# 보안 설정 (로컬에서도 실제 키 사용)
SECRET_KEY = env('DJANGO_SECRET_KEY')
# 디버그 모드 ON (.env에서 DEBUG=True면 True가 됨)
DEBUG = env('DEBUG')
# 접근 허용 도메인 설정 (기본은 localhost만 허용)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["127.0.0.1", "localhost"])

# 로컬 개발용 DB 설정 (SQLite 사용)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Django REST Framework 설정 (세션 기반 인증 사용)
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',  # ✅ 세션 기반
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5,
}

# 디버그 툴바 설정 (로컬 개발용 디버깅 도구)
# INSTALLED_APPS += ['debug_toolbar'] # 앱 추가
# MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware') # 미들웨어 가장 위에 추가
INTERNAL_IPS = ['127.0.0.1'] # 디버그툴바 사용 허용 IP (로컬)