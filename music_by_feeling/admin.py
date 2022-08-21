# /music_by_feeling/admin.py

from django.contrib import admin
from .models import Category, Music_by_feeling, Comment


admin.site.register(Category)
admin.site.register(Music_by_feeling)
admin.site.register(Comment)
