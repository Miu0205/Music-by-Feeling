# Generated by Django 2.1.5 on 2022-10-23 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_by_feeling', '0030_auto_20221018_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='allmusic',
            name='created_year',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='年'),
        ),
        migrations.AddField(
            model_name='favoritemusiclist',
            name='created_year',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='年'),
        ),
        migrations.AddField(
            model_name='music_by_feelinglist',
            name='created_year',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='年'),
        ),
        migrations.AlterField(
            model_name='allmusic',
            name='acousticness',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='アコースティック感'),
        ),
        migrations.AlterField(
            model_name='allmusic',
            name='artist',
            field=models.CharField(max_length=50, null=True, verbose_name='アーティストタイトル'),
        ),
        migrations.AlterField(
            model_name='allmusic',
            name='danceability',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='踊りやすさ'),
        ),
        migrations.AlterField(
            model_name='allmusic',
            name='duration_ms',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='曲の長さ'),
        ),
        migrations.AlterField(
            model_name='allmusic',
            name='energy',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='エネルギッシュ'),
        ),
        migrations.AlterField(
            model_name='allmusic',
            name='instrumentalness',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='ボーカル無し度'),
        ),
        migrations.AlterField(
            model_name='allmusic',
            name='key',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='曲の高さ'),
        ),
        migrations.AlterField(
            model_name='allmusic',
            name='liveness',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='ライブ感'),
        ),
        migrations.AlterField(
            model_name='allmusic',
            name='loudness',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='音圧'),
        ),
        migrations.AlterField(
            model_name='allmusic',
            name='mode',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='スケール'),
        ),
        migrations.AlterField(
            model_name='allmusic',
            name='popularity',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='人気度'),
        ),
        migrations.AlterField(
            model_name='allmusic',
            name='speechiness',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='話し言葉度'),
        ),
        migrations.AlterField(
            model_name='allmusic',
            name='tempo',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='テンポ'),
        ),
        migrations.AlterField(
            model_name='allmusic',
            name='time_signature',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='拍数'),
        ),
        migrations.AlterField(
            model_name='allmusic',
            name='valence',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='ポジティブ'),
        ),
        migrations.AlterField(
            model_name='favoritemusiclist',
            name='acousticness',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='アコースティック感'),
        ),
        migrations.AlterField(
            model_name='favoritemusiclist',
            name='danceability',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='踊りやすさ'),
        ),
        migrations.AlterField(
            model_name='favoritemusiclist',
            name='duration_ms',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='曲の長さ'),
        ),
        migrations.AlterField(
            model_name='favoritemusiclist',
            name='energy',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='エネルギッシュ'),
        ),
        migrations.AlterField(
            model_name='favoritemusiclist',
            name='instrumentalness',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='ボーカル無し度'),
        ),
        migrations.AlterField(
            model_name='favoritemusiclist',
            name='key',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='曲の高さ'),
        ),
        migrations.AlterField(
            model_name='favoritemusiclist',
            name='liveness',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='ライブ感'),
        ),
        migrations.AlterField(
            model_name='favoritemusiclist',
            name='loudness',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='音圧'),
        ),
        migrations.AlterField(
            model_name='favoritemusiclist',
            name='mode',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='スケール'),
        ),
        migrations.AlterField(
            model_name='favoritemusiclist',
            name='popularity',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='人気度'),
        ),
        migrations.AlterField(
            model_name='favoritemusiclist',
            name='speechiness',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='話し言葉度'),
        ),
        migrations.AlterField(
            model_name='favoritemusiclist',
            name='tempo',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='テンポ'),
        ),
        migrations.AlterField(
            model_name='favoritemusiclist',
            name='time_signature',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='拍数'),
        ),
        migrations.AlterField(
            model_name='favoritemusiclist',
            name='track_id',
            field=models.CharField(max_length=100, null=True, verbose_name='track_id'),
        ),
        migrations.AlterField(
            model_name='favoritemusiclist',
            name='valence',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='ポジティブ'),
        ),
        migrations.AlterField(
            model_name='music_by_feelinglist',
            name='acousticness',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='アコースティック感'),
        ),
        migrations.AlterField(
            model_name='music_by_feelinglist',
            name='danceability',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='踊りやすさ'),
        ),
        migrations.AlterField(
            model_name='music_by_feelinglist',
            name='duration_ms',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='曲の長さ'),
        ),
        migrations.AlterField(
            model_name='music_by_feelinglist',
            name='energy',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='エネルギッシュ'),
        ),
        migrations.AlterField(
            model_name='music_by_feelinglist',
            name='instrumentalness',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='ボーカル無し度'),
        ),
        migrations.AlterField(
            model_name='music_by_feelinglist',
            name='key',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='曲の高さ'),
        ),
        migrations.AlterField(
            model_name='music_by_feelinglist',
            name='liveness',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='ライブ感'),
        ),
        migrations.AlterField(
            model_name='music_by_feelinglist',
            name='loudness',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='音圧'),
        ),
        migrations.AlterField(
            model_name='music_by_feelinglist',
            name='mode',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='スケール'),
        ),
        migrations.AlterField(
            model_name='music_by_feelinglist',
            name='popularity',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='人気度'),
        ),
        migrations.AlterField(
            model_name='music_by_feelinglist',
            name='speechiness',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='話し言葉度'),
        ),
        migrations.AlterField(
            model_name='music_by_feelinglist',
            name='tempo',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='テンポ'),
        ),
        migrations.AlterField(
            model_name='music_by_feelinglist',
            name='time_signature',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='拍数'),
        ),
        migrations.AlterField(
            model_name='music_by_feelinglist',
            name='valence',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='ポジティブ'),
        ),
    ]