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







class Music(models.Model):

    category=(
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    )
    feeling_1 = models.CharField(max_length=10, default='5')
    feeling_2 = models.CharField(max_length=10, default='5')
    artist = models.CharField(max_length=20,default='5')

    genre_category = (
      ('1', 'J-POP'),
      ('2', 'K-POP'),
      ('3', 'アニメ'),
      ('4', 'クラシック'),
      ('5', 'ロック'),
    )
    genre = models.CharField(
         'ジャンル',
         max_length=5,
         default='',
         choices=genre_category
         )

    era_category = (
      ('1', '1980'),
      ('2', '1990'),
      ('3', '2000'),
      ('4', '2010'),
      ('5', '2020'),
    )
    era = models.CharField(
         '年代',
         max_length=5,
         default='',
         choices=era_category
         )


    famous = models.BooleanField(default=False)


    def __str__(self):
        return self.artist
