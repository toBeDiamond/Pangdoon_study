# 1. 현재 폴더에서 django 프로젝트(my_pjt)와 앱(my_app)를 만들고 서버를 실행하기 위한 bash 명령어를 주석으로 작성하시오. 

# 프로젝트를 만들기 전 가상환경 'venv'를 먼저 생성합니다. (python -m venv venv)

# 가상환경을 활성화 해줍니다. (source venv/Scripts/activate)

# Django 설치 (pip install Django)

# 의존성 파일을 생성합니다 (pip freeze > requirements.txt)

# Django 프로젝트를 생성합니다. (django-admin startproject my_pjt .)

# 앱 생성 (python manage.py startapp my_app)

# 앱 등록 (settings.py 에 들어가서 INSTALLED_APPS에 'articles'를 넣어줍니다.)

# 서버 실행 (python manage.py runserver)



# 2. http://127.0.0.1:8000/hello로 받은 요청을 통해 my_app 앱의 views.py에 있는 hello 함수를 실행시킬 수 있도록 아래 urls.py를 작성하시오 
from django.urls import path
from my_app import views
urlpatterns = [
    path('hello/', views.hello)
]
