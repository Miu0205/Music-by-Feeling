# /music_by_feeling/models.py

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


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
    title = models.CharField('タイトル', max_length=50, null=True)
    created_at = models.DateTimeField('日付', auto_now_add=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

class AllMusic(models.Model):
    # ユーザー(ユーザー名、パスワード、メールアドレス）
    #user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
 
    tracks = models.CharField('トラックタイトル', max_length=50, null=True)
    artist = models.CharField('アーティストタイトル', max_length=50, null=True)
#    artist = models.IntegerField('アーティストタイトル',blank=True, null=True,default=1)
    danceability = models.FloatField('踊りやすさ',blank=True, null=True,default=0.0)
    energy = models.FloatField('エネルギッシュ',blank=True, null=True,default=0.0)
    key = models.FloatField('曲の高さ',blank=True, null=True,default=0.0)
    loudness = models.FloatField('音圧',blank=True, null=True,default=0.0)
    mode = models.FloatField('スケール',blank=True, null=True,default=0.0)
    speechiness = models.FloatField('話し言葉度',blank=True, null=True,default=0.0)
    acousticness = models.FloatField('アコースティック感',blank=True, null=True,default=0.0)
    instrumentalness = models.FloatField('ボーカル無し度',blank=True, null=True,default=0.0)
    liveness = models.FloatField('ライブ感',blank=True, null=True,default=0.0)
    valence = models.FloatField('ポジティブ',blank=True, null=True,default=0.0)
    tempo = models.FloatField('テンポ',blank=True, null=True,default=0.0)
    type = models.CharField('タイプ', max_length=50, null=True)
    url = models.CharField('URL', max_length=100, null=True)
    track_id = models.CharField('track_id', max_length=100, null=True)
    uri = models.CharField('URI', max_length=100, null=True)
    track_href = models.CharField('曲の詳細情報にアクセスするAPIリンク', max_length=100, null=True)
    analysis_url = models.CharField('曲のオーディオ分析にアクセスするAPIリンク', max_length=100, null=True)
    duration_ms = models.FloatField('曲の長さ',blank=True, null=True,default=0.0)
    time_signature = models.FloatField('拍数',blank=True, null=True,default=0.0)
    artist_url = models.CharField('アーティストURL', max_length=100, null=True)
    genres = models.CharField('ジャンル', max_length=100, null=True)
    popularity = models.IntegerField('人気度',blank=True, null=True,default=0)
    track_url = models.CharField('track_url', max_length=100, null=True)
    created_year = models.IntegerField('年',blank=True, null=True,default=0)
    rank = models.IntegerField('順位',blank=True, null=True,default=0)
    dance_up = models.IntegerField('踊りやすさアップ',blank=True, null=True,default=0)           #danceabilityの"楽"クリック数
    dance_down = models.IntegerField('踊りやすさダウン',blank=True, null=True,default=0)         #danceabilityの"悲"クリック数
    energy_up = models.IntegerField('エネルギッシュアップ',blank=True, null=True,default=0)       #energyの"アクティブ"クリック数
    energy_down = models.IntegerField('エネルギッシュダウン',blank=True, null=True,default=0)     #energyの"落"クリック数
    image_url = models.CharField('イメージURL', max_length=100, null=True)                      #イメージ画像URL

    def __str__(self):
        return self.tracks

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

class Music_by_feelingList(models.Model):
    #ユーザー
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)

    tracks = models.CharField('トラックタイトル', max_length=50, null=True)
    artist = models.CharField('アーティストタイトル', max_length=50, null=True)
#    artist = models.IntegerField('アーティストタイトル',blank=True, null=True,default=1)
    danceability = models.FloatField('踊りやすさ',blank=True, null=True,default=0.0)
    energy = models.FloatField('エネルギッシュ',blank=True, null=True,default=0.0)
    key = models.FloatField('曲の高さ',blank=True, null=True,default=0.0)
    loudness = models.FloatField('音圧',blank=True, null=True,default=0.0)
    mode = models.FloatField('スケール',blank=True, null=True,default=0.0)
    speechiness = models.FloatField('話し言葉度',blank=True, null=True,default=0.0)
    acousticness = models.FloatField('アコースティック感',blank=True, null=True,default=0.0)
    instrumentalness = models.FloatField('ボーカル無し度',blank=True, null=True,default=0.0)
    liveness = models.FloatField('ライブ感',blank=True, null=True,default=0.0)
    valence = models.FloatField('ポジティブ',blank=True, null=True,default=0.0)
    tempo = models.FloatField('テンポ',blank=True, null=True,default=0.0)
    type = models.CharField('タイプ', max_length=50, null=True)
    url = models.CharField('URL', max_length=100, null=True)
    track_id = models.CharField('track_id', max_length=100, null=True)
    uri = models.CharField('URI', max_length=100, null=True)
    track_href = models.CharField('曲の詳細情報にアクセスするAPIリンク', max_length=100, null=True)
    analysis_url = models.CharField('曲のオーディオ分析にアクセスするAPIリンク', max_length=100, null=True)
    duration_ms = models.FloatField('曲の長さ',blank=True, null=True,default=0.0)
    time_signature = models.FloatField('拍数',blank=True, null=True,default=0.0)
    artist_url = models.CharField('アーティストURL', max_length=100, null=True)
    genres = models.CharField('ジャンル', max_length=100, null=True)
    popularity = models.IntegerField('人気度',blank=True, null=True,default=0)
    track_url = models.CharField('track_url', max_length=100, null=True)
    created_year = models.IntegerField('年',blank=True, null=True,default=0)
    rank = models.IntegerField('順位',blank=True, null=True,default=0)
    order = models.IntegerField('通し番号',blank=True, null=True,default=0)
    display_order = models.IntegerField('表示番号',blank=True, null=True,default=0)
    dance_up = models.IntegerField('踊りやすさアップ',blank=True, null=True,default=0)           #danceabilityの"楽"クリック数
    dance_down = models.IntegerField('踊りやすさダウン',blank=True, null=True,default=0)         #danceabilityの"悲"クリック数
    energy_up = models.IntegerField('エネルギッシュアップ',blank=True, null=True,default=0)       #energyの"アクティブ"クリック数
    energy_down = models.IntegerField('エネルギッシュダウン',blank=True, null=True,default=0)     #energyの"落"クリック数
    image_url = models.CharField('イメージURL', max_length=100, null=True)                      #イメージ画像URL

    def __str__(self):
        return self.tracks

class Music_by_feeling_History(models.Model):
    tracks = models.CharField('トラックタイトル', max_length=50, null=True)
    artist = models.CharField('アーティストタイトル', max_length=50, null=True)
#    artist = models.IntegerField('アーティストタイトル',blank=True, null=True,default=1)
    danceability = models.FloatField('踊りやすさ',blank=True, null=True,default=0.0)
    energy = models.FloatField('エネルギッシュ',blank=True, null=True,default=0.0)
    key = models.FloatField('曲の高さ',blank=True, null=True,default=0.0)
    loudness = models.FloatField('音圧',blank=True, null=True,default=0.0)
    mode = models.FloatField('スケール',blank=True, null=True,default=0.0)
    speechiness = models.FloatField('話し言葉度',blank=True, null=True,default=0.0)
    acousticness = models.FloatField('アコースティック感',blank=True, null=True,default=0.0)
    instrumentalness = models.FloatField('ボーカル無し度',blank=True, null=True,default=0.0)
    liveness = models.FloatField('ライブ感',blank=True, null=True,default=0.0)
    valence = models.FloatField('ポジティブ',blank=True, null=True,default=0.0)
    tempo = models.FloatField('テンポ',blank=True, null=True,default=0.0)
    type = models.CharField('タイプ', max_length=50, null=True)
    url = models.CharField('URL', max_length=100, null=True)
    track_id = models.CharField('track_id', max_length=100, null=True)
    uri = models.CharField('URI', max_length=100, null=True)
    track_href = models.CharField('曲の詳細情報にアクセスするAPIリンク', max_length=100, null=True)
    analysis_url = models.CharField('曲のオーディオ分析にアクセスするAPIリンク', max_length=100, null=True)
    duration_ms = models.FloatField('曲の長さ',blank=True, null=True,default=0.0)
    time_signature = models.FloatField('拍数',blank=True, null=True,default=0.0)
    artist_url = models.CharField('アーティストURL', max_length=100, null=True)
    genres = models.CharField('ジャンル', max_length=100, null=True)
    popularity = models.IntegerField('人気度',blank=True, null=True,default=0)
    track_url = models.CharField('track_url', max_length=100, null=True)
    created_year = models.IntegerField('年',blank=True, null=True,default=0)
    rank = models.IntegerField('順位',blank=True, null=True,default=0)
    order = models.IntegerField('通し番号',blank=True, null=True,default=0)
    display_order = models.IntegerField('表示番号',blank=True, null=True,default=0)
    dance_up = models.IntegerField('踊りやすさアップ',blank=True, null=True,default=0)           #danceabilityの"楽"クリック数
    dance_down = models.IntegerField('踊りやすさダウン',blank=True, null=True,default=0)         #danceabilityの"悲"クリック数
    energy_up = models.IntegerField('エネルギッシュアップ',blank=True, null=True,default=0)       #energyの"アクティブ"クリック数
    energy_down = models.IntegerField('エネルギッシュダウン',blank=True, null=True,default=0)     #energyの"落"クリック数
    image_url = models.CharField('イメージURL', max_length=100, null=True)                      #イメージ画像URL

    def __str__(self):
        return self.tracks

class Music_by_feeling_Selection_History(models.Model):
    danceability = models.FloatField('踊りやすさ',blank=True, null=True,default=0.0)
    energy = models.FloatField('エネルギッシュ',blank=True, null=True,default=0.0)
    artist = models.CharField('アーティスト名', max_length=50, null=True)
    period = models.IntegerField('年代',blank=True, null=True,default=0)              #選択なしの時は0が入る
    genres = models.CharField('ジャンル', max_length=100, null=True)
    popularity = models.BooleanField('人気の曲から選ぶ',default=False, blank=True)
    date = models.DateTimeField('実施日',default=timezone.now)

    def __str__(self):
        return self.date.strftime("%Y/%m/%d %H:%M:%S")

class FavoriteMusicList(models.Model):
    #ユーザー
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)

    tracks = models.CharField('トラックタイトル', max_length=50, null=True)
    artist = models.CharField('アーティストタイトル', max_length=50, null=True)
#    artist = models.IntegerField('アーティストタイトル',blank=True, null=True,default=1)
    danceability = models.FloatField('踊りやすさ',blank=True, null=True,default=0.0)
    energy = models.FloatField('エネルギッシュ',blank=True, null=True,default=0.0)
    key = models.FloatField('曲の高さ',blank=True, null=True,default=0.0)
    loudness = models.FloatField('音圧',blank=True, null=True,default=0.0)
    mode = models.FloatField('スケール',blank=True, null=True,default=0.0)
    speechiness = models.FloatField('話し言葉度',blank=True, null=True,default=0.0)
    acousticness = models.FloatField('アコースティック感',blank=True, null=True,default=0.0)
    instrumentalness = models.FloatField('ボーカル無し度',blank=True, null=True,default=0.0)
    liveness = models.FloatField('ライブ感',blank=True, null=True,default=0.0)
    valence = models.FloatField('ポジティブ',blank=True, null=True,default=0.0)
    tempo = models.FloatField('テンポ',blank=True, null=True,default=0.0)
    type = models.CharField('タイプ', max_length=50, null=True)
    url = models.CharField('URL', max_length=100, null=True)
    track_id = models.CharField('track_id', max_length=100, null=True)
    uri = models.CharField('URI', max_length=100, null=True)
    track_href = models.CharField('曲の詳細情報にアクセスするAPIリンク', max_length=100, null=True)
    analysis_url = models.CharField('曲のオーディオ分析にアクセスするAPIリンク', max_length=100, null=True)
    duration_ms = models.FloatField('曲の長さ',blank=True, null=True,default=0.0)
    time_signature = models.FloatField('拍数',blank=True, null=True,default=0.0)
    artist_url = models.CharField('アーティストURL', max_length=100, null=True)
    genres = models.CharField('ジャンル', max_length=100, null=True)
    popularity = models.IntegerField('人気度',blank=True, null=True,default=0)
    track_url = models.CharField('track_url', max_length=100, null=True)
    created_year = models.IntegerField('年',blank=True, null=True,default=0)
    rank = models.IntegerField('順位',blank=True, null=True,default=0)
    order = models.IntegerField('通し番号',blank=True, null=True,default=0)
    display_order = models.IntegerField('表示番号',blank=True, null=True,default=0)
    dance_up = models.IntegerField('踊りやすさアップ',blank=True, null=True,default=0)           #danceabilityの"楽"クリック数
    dance_down = models.IntegerField('踊りやすさダウン',blank=True, null=True,default=0)         #danceabilityの"悲"クリック数
    energy_up = models.IntegerField('エネルギッシュアップ',blank=True, null=True,default=0)       #energyの"アクティブ"クリック数
    energy_down = models.IntegerField('エネルギッシュダウン',blank=True, null=True,default=0)     #energyの"落"クリック数
    image_url = models.CharField('イメージURL', max_length=100, null=True)                      #イメージ画像URL

    def __str__(self):
        return self.tracks

class Music(models.Model):

    # ユーザー(ユーザー名、パスワード、メールアドレス）
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)

    feeling_1 = models.CharField(max_length=10, default='5')
    feeling_2 = models.CharField(max_length=10, default='5')
    artist = models.CharField(max_length=20,default='5',blank=True, null=True)
    genre = models.CharField(
         max_length=10,
         default='',
         blank=True,
         null=True
         )
    era = models.CharField(
         '年代',
         max_length=5,
         default='0',
         blank=True,
         null=True
         )
    date = models.DateTimeField('日付', null=True)
    famous = models.BooleanField(default=False, blank=True, null=True)
    """time = models.DateTimeField(default=timezone.now)"""

    def __str__(self):
        return str(self.date)

class History(models.Model):
    #ユーザー
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)

    tracks = models.CharField('トラックタイトル', max_length=50, null=True)
    artist = models.CharField('アーティストタイトル', max_length=50, null=True)
    artist = models.IntegerField('アーティストタイトル',blank=True, null=True,default=1)
    danceability = models.FloatField('踊りやすさ',blank=True, null=True,default=0.0)
    energy = models.FloatField('エネルギッシュ',blank=True, null=True,default=0.0)
    key = models.FloatField('曲の高さ',blank=True, null=True,default=0.0)
    loudness = models.FloatField('音圧',blank=True, null=True,default=0.0)
    mode = models.FloatField('スケール',blank=True, null=True,default=0.0)
    speechiness = models.FloatField('話し言葉度',blank=True, null=True,default=0.0)
    acousticness = models.FloatField('アコースティック感',blank=True, null=True,default=0.0)
    instrumentalness = models.FloatField('ボーカル無し度',blank=True, null=True,default=0.0)
    liveness = models.FloatField('ライブ感',blank=True, null=True,default=0.0)
    valence = models.FloatField('ポジティブ',blank=True, null=True,default=0.0)
    tempo = models.FloatField('テンポ',blank=True, null=True,default=0.0)
    type = models.CharField('タイプ', max_length=50, null=True)
    url = models.CharField('URL', max_length=100, null=True)
    track_id = models.CharField('track_id', max_length=100, null=True)
    uri = models.CharField('URI', max_length=100, null=True)
    track_href = models.CharField('曲の詳細情報にアクセスするAPIリンク', max_length=100, null=True)
    analysis_url = models.CharField('曲のオーディオ分析にアクセスするAPIリンク', max_length=100, null=True)
    duration_ms = models.FloatField('曲の長さ',blank=True, null=True,default=0.0)
    time_signature = models.FloatField('拍数',blank=True, null=True,default=0.0)
    artist_url = models.CharField('アーティストURL', max_length=100, null=True)
    genres = models.CharField('ジャンル', max_length=100, null=True)
    popularity = models.IntegerField('人気度',blank=True, null=True,default=0)
    track_url = models.CharField('track_url', max_length=100, null=True)
    created_year = models.IntegerField('年',blank=True, null=True,default=0)
    rank = models.IntegerField('順位',blank=True, null=True,default=0)
    order = models.IntegerField('通し番号',blank=True, null=True,default=0)
    display_order = models.IntegerField('表示番号',blank=True, null=True,default=0)
    dance_up = models.IntegerField('踊りやすさアップ',blank=True, null=True,default=0)           #danceabilityの"楽"クリック数
    dance_down = models.IntegerField('踊りやすさダウン',blank=True, null=True,default=0)         #danceabilityの"悲"クリック数
    energy_up = models.IntegerField('エネルギッシュアップ',blank=True, null=True,default=0)       #energyの"アクティブ"クリック数
    energy_down = models.IntegerField('エネルギッシュダウン',blank=True, null=True,default=0)     #energyの"落"クリック数
    image_url = models.CharField('イメージURL', max_length=100, null=True)                      #イメージ画像URL

    def __str__(self):
        return self.tracks

class Account(models.Model):

    # ユーザー認証のインスタンス(1vs1関係)
    # ユーザー(ユーザー名、パスワード、メールアドレス）
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)

    # 追加フィールド
    age=models.SmallIntegerField()
    sex_category=(('1','male'),('2','female'),('3','other'))

    sex=models.CharField(max_length=3,default='',choices=sex_category,blank=True)

    def __str__(self):
        return str(self.user)
