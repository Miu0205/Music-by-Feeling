# /project/urls.py

from django.contrib import admin
from django.views.generic import TemplateView #デフォルトページ
#from django.contrib.auth.decorators import login_required #ログイン認証
from django.urls import path, include  # ←追記
from todo import views #新規登録

index_view = TemplateView.as_view(template_name="todo/index.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),  # ←追記
    #path("", login_required(index_view), name="index"), #loginが認証されたら、index.htmlに飛ぶ。ログインが必須になる。
    #path("signup/", views.SignUpView.as_view(), name="signup"), #新規登録
    #path('activate/<uidb64>/<token>/', views.ActivateView.as_view(), name='activate'), #新規登録のメール結果画面
    #path('accounts/', include('allauth.urls')), #allauth
]
