# /music_by_feeling/models.py

from django.db import models
from django.utils import timezone


"""カテゴリー"""
class Category(models.Model):
    title = models.CharField('タイトル', max_length=20)

    """self.titleとすることでadmin管理画面にてインスタンス変数として表示される"""
    def __str__(self):
        return self.title


"""
タイトル、日付テーブルとカテゴリーを紐づけるためのテーブル。
PROTECTは紐づいているデータが存在すれば消されない
"""
class Music_by_feeling(models.Model):
    title = models.CharField('タイトル', max_length=50)
    created_at = models.DateTimeField('日付', auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
