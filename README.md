# okpos-project

## 충돌 방지를 위한 가상환경 설정
python -m venv .venv / 3.8버전 강제 : py -3.8 -m venv .venv

source .venv/bin/activate / Windows : .venv\Scripts\activate.bat

pip install --upgrade pip

pip install -r requirements.txt

## 로컬 Django 실행

python manage.py migrate

python manage.py runserver

localhost:8000/doc/

## Docker 빌드 및 실행

docker-compose build

docker-compose up

localhost:8000/doc/


## 테스트 진행

coverage run -m pytest

coverage report
