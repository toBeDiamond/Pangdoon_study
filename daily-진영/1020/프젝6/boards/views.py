from django.shortcuts import render, redirect, get_object_or_404
from .models import Board, Comment
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from .forms import BoardForm, CommentForm

# Create your views here.
def index(request):    
    # 전체 글 조회하는 웹페이지 만들어주기
    # 1. 전체 글 조회
    boards = Board.objects.all()
    # 전체글을 가져와주는데 / 우리가 설정해준 테이블에서 모든 것을 가져온다.
    context = {
        'boards':boards
        # 그 모든 것을 context로 묶어서 render함수에다가 같이 보내줌
    }
    # 2. 웹페이지 만들어주기
    return render(request, 'boards/index.html', context)


@require_http_methods(['GET','POST'])
@login_required
#위에서 dvd.http에서 선언해준 데코레이터! 
def create(request):
    if request.method == 'POST':
        # 실제로 값을 입력받았을 때
        form = BoardForm(request.POST)
        # 우리가 만든 BoardForm에 입력받은 값을 넣어준다.
        if form.is_valid():
            # 유효성 검사를해주고 
            board = form.save(commit=False)
            # 임시서장을 해주는 이유 : 우리가 생성해줄 페이지에 필요한 필드를 title과 content 두가지로 제한하였다.
            # 그렇지만 실제로 필요한 것은 author (작성자)가 필요하다. 그렇기 때문에 임시저장을 통해서 
            # user 를 받아주고 넘겨주어서 저장을 같이 해주어야 한다. 
            # 미완성된 board 객체를 user를 넣어주면서 완벽하게 해주어야 하기때문에 이렇게 저장하였다.
            board.author = request.user
            # 미완성된 board에서 필요했던 author 필드의 값을 넣어주면서 완벽하게 만들어준다.
            form.save() 
            return redirect('boards:index')

    else:
        # 만약 만들어줘 라는 요청이 아닐 시에는 생성페이지를 보여주어야 한다.
        form = BoardForm()
    context = {
        'form':form
    }
    return render(request, 'boards/create.html', context)


@require_http_methods(['GET','POST']) 
def detail(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    if request.method == 'POST':
        # detail 에서 POST 요청을 받는다는 뜻은 삭제를 하겠다는 말이다.
        board.delete()
        # 삭제를 해준다.
        return redirect('boards:index')
        # 삭제를 해준뒤에 detail이 삭제되었으니까 index 페이지로 보낸다.

    else:
        form = CommentForm()
        comments = board.comment_set.all()
        # 역참조 발생!!
        # 역참조 매니저를 써줘야 하는데, 이는 자동으로 생성되며
        # (모델명:소문자)_set의 이름 형식을 가지고있다!
        # 쓰는 방법은 .objects 매니저와 동일하다!
        context = {
            'board':board,
            # 요청해준 상세페이지를 단순히 보여주기만 한다.
            'form': form,
            # 댓글 생성 폼도 같이 보내줘야한다.
            'comments': comments,
            # board를 역참조하여, 댓글들을 모두 들고왔다.
        }
    return render(request,'boards/detail.html', context)



@require_http_methods(['GET','POST']) 
def update(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    # 기존의 내가 썼던 board를 그대로 가져와 줘야하므로 Board의 고유 pk를 찾아서 가져옴
    if request.method == 'POST':
        form = BoardForm(data=request.POST, instance=board)
        # 수정되기 전 나의 board는 instance로 가져온다(이전의 나의 수정되기 전 것)
        # 수정유무는 요청값과 같이 instance 값까지 가지고오냐마냐로 판단할 수 있다.
        # 내가 직접 수정한 것은 request.POST이고 그것을 data에 넣는다. 
        if form.is_valid():
            # board = form.save(commit=False)
            # board.author = request.user
            # 필요 없는 이유 : 이미 가져와준 board 에서 이미 author 값이 담겨져있기 때문에
            # 굳이 추가로 넣어줄 필요가 없다. 
            form.save()
            return redirect('boards:index')

    else:
        form = BoardForm(instance=board)
        # BoardForm에 나의 고유 board를 넣어준 값을 보여준다. (get 요청일 경우)
    context = {
        'form':form,
        'board':board,
    }
    return render(request, 'boards/update.html', context)


@require_http_methods(['POST']) 
def comment(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    # 내가 어떤 board에다가 댓글을 달지 그 board를 가져와주는 것
    comment = CommentForm(request.POST)
    # 댓글을 CommentForm에 입력값으로 넣어준다. 코멘트 폼에서 사용하는 필드는 content 만 !
    if comment.is_valid():
        comment = comment.save(commit=False)
        # 임시저장을 해주고
        comment.author = request.user
        # 웹페이지에서 보여줘야할 것은 누가 쓴 글인지이기 때문에..
        comment.board = board
        # 어떤 글에 댓글을 작성해주었는지 지정해주어야 하기때문에
        comment.save()
    return redirect('boards:detail', board_pk)


def comment_detail(request, board_pk, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    # get_object_or_404 같은 경우는 (모델명, 찾아온 데이터) -> DB에 없는 데이터를 참조하려 시도하면
    # 원래는 500번대의 에러(서버에러) 가 나는데, 404번 오류(NOT FOUND: 없음)를 보내준다. 
    comment.delete()
    return redirect('boards:detail', board_pk)
