# /project/urls.py

from django.contrib import admin
from django.urls import path, include  # ←追記


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('music_by_feeling.urls')),  # ←追記
]
