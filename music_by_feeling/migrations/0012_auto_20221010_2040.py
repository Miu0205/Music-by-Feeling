# Generated by Django 2.1.5 on 2022-10-10 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_by_feeling', '0011_auto_20221010_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allmusic',
            name='acousticness',
            field=models.FloatField(blank=True, default=1.0, null=True, verbose_name='アコースティック感'),
        ),
        migrations.AlterField(
            model_name='allmusic',
            name='danceability',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='踊りやすさ'),
        ),
        migrations.AlterField(
            model_name='allmusic',
            name='energy',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='エネルギッシュ'),
        ),
        migrations.AlterField(
            model_name='allmusic',
            name='instrumentalness',
            field=models.FloatField(blank=True, default=1.0, null=True, verbose_name='ボーカル無し度'),
        ),
        migrations.AlterField(
            model_name='allmusic',
            name='key',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='曲の高さ'),
        ),
        migrations.AlterField(
            model_name='allmusic',
            name='liveness',
            field=models.FloatField(blank=True, default=1.0, null=True, verbose_name='ライブ感'),
        ),
        migrations.AlterField(
            model_name='allmusic',
            name='loudness',
            field=models.FloatField(blank=True, default=1.0, null=True, verbose_name='音圧'),
        ),
        migrations.AlterField(
            model_name='allmusic',
            name='mode',
            field=models.FloatField(blank=True, default=1.0, null=True, verbose_name='スケール'),
        ),
        migrations.AlterField(
            model_name='allmusic',
            name='speechiness',
            field=models.FloatField(blank=True, default=1.0, null=True, verbose_name='話し言葉度'),
        ),
        migrations.AlterField(
            model_name='allmusic',
            name='tempo',
            field=models.FloatField(blank=True, default=1.0, null=True, verbose_name='テンポ'),
        ),
        migrations.AlterField(
            model_name='allmusic',
            name='type',
            field=models.FloatField(blank=True, default=1.0, null=True, verbose_name='タイプ'),
        ),
        migrations.AlterField(
            model_name='allmusic',
            name='url',
            field=models.CharField(max_length=100, null=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='allmusic',
            name='valence',
            field=models.FloatField(blank=True, default=1.0, null=True, verbose_name='ポジティブ'),
        ),
    ]