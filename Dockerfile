FROM python:3.12.3

# 로그 출력용
RUN echo "Django_3_22 deploy 2025.04.01 00:00"

# 작업 디렉토리
WORKDIR /home/

# 소스코드 복제 (CI/CD 자동화 시에만 적합)
RUN git clone https://github.com/handgonpo/django_3_22.git -b main

# 프로젝트 폴더로 이동
WORKDIR /home/django_3_22/

# 시스템 패키지 설치 (PostgreSQL 연동용)
RUN apt update && apt install -y libpq-dev gcc python3-dev

# Python 패키지 설치 + requirements 설치
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# 포트 개방
EXPOSE 8000

# 컨테이너 시작 시 실행될 명령
CMD ["gunicorn", "config.wsgi", "--env", "DJANGO_SETTINGS_MODULE=config.settings.deploy", "--bind", "0.0.0.0:8000", "--timeout", "60"]