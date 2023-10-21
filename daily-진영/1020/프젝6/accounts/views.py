from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout as auth_logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm



# Create your views here.
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # AuthenticationForm은 이미 만들어진 폼(모델폼 아님 주의)
        # 사용방법을 잘 알고 있어야한다! 매개변수는 두 가지(request, 데이터)가 들어간다.
        if form.is_valid():
            auth_login(request, form.get_user())
            # .get_user()는 AuthenticationForm에서 입력받은 userdata를 받아오는 메서드
            # 장고가 기본적으로 제공하는 기능을 사용하기 위해서는 필요한 데이터가 무엇이 들어가는지 확인해야합니다.
            # vscode가 필요한 매개변수를 잘 알려줍니다. (소괄호에 마우스 커서 올리면 보임)
            return redirect(request.GET.get('next') or 'boards:index')
                    # @login_required에 걸리고 로그인 시도할 때,
                    # POST와 함께 next에 데이터를 담은 GET요청도 함께 들어온다
                    # 이 GET에서 next를 읽어와서 @login_required에 걸리기 이전 페이지로 redirect 해 준다.
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request,'accounts/login.html', context)


@require_http_methods(['POST'])
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('boards:index')


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            # 회원가입과 동시에 로그인도 진행해줌 : 오류는 안 남 <-- 유저 친화적인 설계
            return redirect('boards:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def profile(request, user_pk):
    User = get_user_model()
    # get_user_model()의 리턴값을 User변수에 넣어주자
    owner = get_object_or_404(User, pk=user_pk)
    boards = owner.board_set.all()
    comments = owner.comment_set.all()
    followings = owner.followings.all()
    followers = owner.followers.all()
    context = {
        'owner': owner,
        'boards': boards,
        'comments': comments,
        'followers': followers,
        'followings': followings,
    }
    return render(request, 'accounts/profile.html', context)



@login_required
def follow(request, user_pk):
    if request.method == 'POST':
        User = get_user_model()
        followed = get_object_or_404(User, pk=user_pk)
        # if request.user in followed.followers.all(): # 멤버십 연산자 in이 너무 느려
        if followed.followers.filter(pk=request.user.pk).exists():
        # 버튼을 눌린 사람의 팔로워들 중에 현재 로그인한 사람이 포함되어있으면 : 언팔 버튼 누른거
            followed.followers.remove(request.user)
        else:
            followed.followers.add(request.user)
    
    return redirect('accounts:profile', user_pk)


