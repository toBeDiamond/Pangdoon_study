from django.contrib import admin
from .models import User
# admin 사이트에 등록할 (우리가 만든) 모델을 가져옴
from django.contrib.auth.admin import UserAdmin   
# 외우기 / 장고에 있는 인증관련 기본앱 중, 관리자파일에서 사용할 것들을 미리만들어준 모듈을 가져옴


# Register your models here.
admin.site.register(User, UserAdmin)
# 여기서 등록 / 관리자 사이트 등록 (모델명, 모듈가져 온 것)
