from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    # 중개모델 필드는 ManyToMany이고 followings 는 자기자신을 참조하기 때문에 'self'를 넣고
    # symmetrical(대칭) 여부를 설정한다. 만약에 대칭관계가 필요하면 True이다. 예를들어서
    # 내가 상대방을 팔로잉하면 자동으로 상대방도 나를 팔로잉하게 된다. 그렇기때문에 False로 해주었다. 
    # 그리고 역참조 시에 사용될 이름을 related_name 으로 설정해주었다.
