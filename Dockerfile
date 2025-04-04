FROM python:3.12.3

RUN echo "Django3_22 deploy 2025.04.01 16:00"

# 작업 디렉토리 설정
WORKDIR /home/

# GitHub에서 소스코드 클론
RUN git clone https://github.com/handgonpo/django_3_22.git -b main

# 프로젝트 폴더 기준으로 이동
WORKDIR /home/django_3_22

# pip 업그레이드 및 의존성 설치
RUN pip install -r requirements.txt

RUN apt update

# pip 업그레이드 및 의존성 설치
RUN mkdir -p /home/django_3_22/staticfiles
RUN mkdir -p /home/django_3_22/db

# 포트 개방
EXPOSE 8000

# 환경 변수 설정
ENV DJANGO_SETTINGS_MODULE=config.settings.deploy

# 시작 명령어
CMD ["bash", "-c", "git pull && python manage.py collectstatic --noinput && python manage.py migrate && gunicorn config.wsgi --bind 0.0.0.0:8000 --timeout 60"]