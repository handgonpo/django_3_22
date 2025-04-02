# 배포 환경 설정

from .base import *

# 시크릿 파일 읽기
# 수동방식
# def read_secret(secret_name):
#     file = open("/run/secrets/" + secret_name)
#     secret = file.read()
#     secret = secret.rstrip().lstrip()
#     file.close()
#     return secret

# 시크릿 파일 읽기
def read_secret(secret_name):
    with open("/run/secrets/" + secret_name) as file:
        return file.read().strip()


# 보안 SECURITY WARNING: keep the secret key used in production secret! 
SECRET_KEY = read_secret('DJANGO_SECRET_KEY')
DEBUG = True
ALLOWED_HOSTS = ['yourdomain.com'] # 도메인 생기면 변경

# 추가보안설정
SECURE_BROWSER_XSS_FILTER = True  # 보안 헤더 설정
SECURE_CONTENT_TYPE_NOSNIFF = True # MIME 타입 보안
CSRF_COOKIE_SECURE = True # HTTPS 환경에서만 쿠키
SESSION_COOKIE_SECURE = True # HTTPS 환경에서만 세션 쿠키

# 데이터베이스 (PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': read_secret('POSTGRES_DB'),
        'USER': read_secret('POSTGRES_USER'),
        'PASSWORD': read_secret('POSTGRES_PASSWORD'),
        'HOST': 'postgresdb',
        'PORT': '5432', # PostgreSQL의 기본 포트 
    }
}

#  DRF 설정 API 요청에 대한 접근 권한(permissions) 을 어떻게 처리할지를 지정
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',  # ✅ 세션 기반
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5,
}   

STATIC_ROOT = "/home/django_3_22/staticfiles" # 내경로가 아닌 도커 경로에 맞춰야 함
# deploy.py(static_volume:/data/static) 연결
# nginx.conf(location /static/ {alias /data/static/;})