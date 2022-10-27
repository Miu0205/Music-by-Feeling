from django import forms

from .models import Comment, Account

from django.contrib.auth.models import User #ログイン、新規登録用

from .models import Music
from django.utils import timezone

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)


class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ('feeling_1','feeling_2','artist','genre', 'era', 'famous' )

# フォームクラス作成
class AccountForm(forms.ModelForm):
    # パスワード入力：非表示対応
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")

    class Meta():
        # ユーザー認証
        model = User
        # フィールド指定
        fields = ('username','email','password')
        # フィールド名指定
        labels = {'username':"ユーザーID",'email':"メール"}

class AddAccountForm(forms.ModelForm):
    class Meta():
        # モデルクラスを指定
        model = Account
        fields = ('age','sex',)
        labels = {'age':"年齢",'sex':"性別",}
