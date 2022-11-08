# /music_by_feeling/urls.py

from django.urls import path
from . import views


app_name = 'music_by_feeling'

urlpatterns = [
        path('', views.index, name='index'),  # ←一覧
        path('<int:id>/delete/', views.delete, name='delete'),  # ←削除機能用
        path('music_by_feeling/<str:category>/', views.music_by_feeling_category, name='music_by_feeling_category'),  # ←カテゴリ
        path('videoplayback', views.videoplayback, name='videoplayback'),    # ←追加
        path('playlist', views.playlist, name='playlist'),    # ←追加
        path('spotifyLoad', views.spotifyLoad, name='spotifyLoad'),    # ←追加
        path('maintenance', views.maintenance, name='maintenance'),    # ←追加

        path('page3/', views.music_render, name='page3'),  # ３

        path('music_list/',views.MusicList.as_view(), name='music_list'),
        path('FavoriteMusicList_list/',views.LikeList.as_view(), name='like_list'),
        path('History_list/',views.HistoryList.as_view(), name='history_list'),

        #spath('signup', views.SignUpView.as_view(), name="signup"),
        #path('logout',views.logout, name="logout"),

        
]
