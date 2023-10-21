from django import forms
from .models import Board, Comment

class BoardForm(forms.ModelForm):
    class Meta:
        # 어떤 테이블에서 가져올 것인지 적어주고,
        model = Board
        # 테이블에서 필요한 필드 값만 가져온다. 
        fields = ("title", "content")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)