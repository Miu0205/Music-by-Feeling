# /project/urls.py

from django.contrib import admin
from django.urls import path, include  # ←追記

from django.conf.urls.static import static #追加
from django.conf import settings #追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('music_by_feeling.urls')),  # ←追記
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #追加
