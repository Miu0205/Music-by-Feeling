# /music_by_feeling/admin.py

from django.contrib import admin
from .models import Category, Music_by_feeling, Comment, AllMusic, Music, Music_by_feelingList, Music_by_feeling_History, Music_by_feeling_Selection_History, FavoriteMusicList, History, Account


admin.site.register(Category)
admin.site.register(Music_by_feeling)
admin.site.register(Comment)
admin.site.register(Music_by_feelingList)
admin.site.register(Music_by_feeling_History)
admin.site.register(Music_by_feeling_Selection_History)
admin.site.register(FavoriteMusicList)
admin.site.register(History)
admin.site.register(Account)

admin.site.register(AllMusic)
admin.site.register(Music)
