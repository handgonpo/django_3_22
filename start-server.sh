#!/bin/bash
# start-server.sh

echo "Moving to project folder..."
cd ~/django_3_22 || exit

echo "Activating virtual environment..."
source venv/bin/activate

echo "Starting Gunicorn server..."
gunicorn --bind 127.0.0.1:8000 config.wsgi:application

# 테스트용으로 외부 브라우저에서 직접 접속하려면:
# --bind 0.0.0.0:8000