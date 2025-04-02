FROM python:3.12.3

# 로그용 메시지
RUN echo "▶ Django_3_22 배포 준비 - 2025.04.01"

# 필수 패키지 설치 (PostgreSQL 연동을 위한 라이브러리)
RUN apt update && apt install -y libpq-dev gcc python3-dev git

# 작업 디렉토리 설정
WORKDIR /home/app

# GitHub에서 소스코드 클론
RUN git clone https://github.com/handgonpo/django_3_22.git -b main

# 프로젝트 폴더 기준으로 이동
WORKDIR /home/app/django_3_22

# pip 업그레이드 및 의존성 설치
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# 포트 개방
EXPOSE 8000

# gunicorn 명령 실행 (배포 설정 사용)
CMD ["gunicorn", "config.wsgi", "--env", "DJANGO_SETTINGS_MODULE=config.settings.deploy", "--bind", "0.0.0.0:8000", "--timeout", "60"]
