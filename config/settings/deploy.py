from .base import *
import os

# 환경변수에서 직접 읽기
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
DEBUG = True
ALLOWED_HOSTS = ['*']  # 테스트용으로 전체 허용, 배포 시 도메인으로 변경

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# SQLite3 설정
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.environ.get('DATABASE_NAME', os.path.join(BASE_DIR, 'db.sqlite3')),
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5,
}

STATIC_ROOT = "/home/django_3_22/staticfiles"
