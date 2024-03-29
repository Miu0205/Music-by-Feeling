# /music_by_feeling/urls.py

from django.urls import path
from . import views


app_name = 'music_by_feeling'

urlpatterns = [
        path('', views.index, name='index'),  # ←一覧
        path('<int:id>/delete/', views.delete, name='delete'),  # ←削除機能用
        path('music_by_feeling/<str:category>/', views.music_by_feeling_category, name='music_by_feeling_category'),  # ←カテゴリ
        
        path('<int:id>/videoplayback', views.videoplayback, name='videoplayback'),    # ←追加
        path('<int:id>/spotifyLoad', views.spotifyLoad, name='spotifyLoad'),    # ←追加
        path('<int:id>/feedback', views.feedback, name='feedback'),    # ←追加
        path('maintenance', views.maintenance, name='maintenance'),    # ←追加
        path('graph', views.graph, name='graph'),    # ←追加

        path('<int:id>/page3/', views.music_render, name='page3'),  # ３
        #path('page3_conf/<int:pk>', views.page3_conf, name='page3_conf'), #1/25

        path('<int:id>/playlist', views.playlist, name='playlist'),    # ←追加
        path('<int:id>/playlist_null', views.playlistNull, name='playlist_null'),    # ←追加
        path('<int:id>/music_list/',views.MusicList.as_view(), name='music_list'),
        path('<int:id>/History_list/',views.HistoryList, name='history_list'),
        path('<int:id>/History_null/',views.historyNull, name='history_null'),

        path('login/', views.Login, name='login'),
        path('signup/', views.Signup, name="signup"),
        path('logout/',views.Logout, name="logout"),


        ]


'''
        #path('videoplayback', views.videoplayback, name='videoplayback'),    # ←追加
        #path('spotifyLoad', views.spotifyLoad, name='spotifyLoad'),    # ←追加
        #path('graph', views.graph, name='graph'),    # ←追加
        #path('page3/', views.music_render, name='page3'),  # ３
        #path('page3_conf/<int:pk>', views.page3_conf, name='page3_conf'), #1/25

        #path('playlist', views.playlist, name='playlist'),    # ←追加
        #path('playlist_null', views.playlistNull, name='playlist_null'),    # ←追加
        #path('music_list/',views.MusicList.as_view(), name='music_list'),
        #path('History_list/',views.HistoryList, name='history_list'),
        #path('History_null/',views.historyNull, name='history_null'),
'''
