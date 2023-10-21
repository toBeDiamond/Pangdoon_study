from django.contrib.auth.forms import UserCreationForm
# UserCreationForm(얘 모델폼임) 을 써야하는데
# 등록된 모델이 기존의 디폴트 모델임
# 커스텀 유저모델을 쓰고있기 때문에 오버라이딩(재정의)를 통해서 쓸만하게 바꿔줘야함
from django.contrib.auth import get_user_model
# models.py 랑 admin.py에서 사이트 등록할 때 빼고 항상 get_user_model()함수를 써서 현재 활성화된 User모델을 가져옴
# 이거 말고 다른 방법들
# 1. django.conf.settings.AUTH_USER_MODEL을 들고오는 방법 : models.py에서만!
# 2. form .models import User : 얘는 안 씀 --> 사후관리가 힘들어

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        