from django.db import models
# from accounts.models import User 는 오류가 날 수 있다. 
from django.conf import settings
# 모델에서만 쓰이는 방법/ 다른 곳에서는 get_user_model()을 사용한다.
# 장고 전체구조에서 세팅을 가져옴

# Create your models here.
class Board(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 세팅에서 가져온 AUTH_USER_MODEL 을 사용 (우리가 직접 세팅에서 등록한 것)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Board와 Comment를 연결시켜줌 ( 외래키를 통해 ) 
    # 1 : N  //  Board : Comment 
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

