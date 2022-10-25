# Generated by Django 2.1.5 on 2022-10-10 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_by_feeling', '0008_auto_20221010_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllMusics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracks', models.CharField(max_length=50, null=True, verbose_name='トラックタイトル')),
                ('artist', models.CharField(max_length=50, null=True, verbose_name='アーティストタイトル')),
                ('danceability', models.IntegerField(blank=True, default=1, null=True, verbose_name='踊りやすさ')),
                ('energy', models.IntegerField(blank=True, default=1, null=True, verbose_name='エネルギッシュ')),
                ('key', models.IntegerField(blank=True, default=1, null=True, verbose_name='曲の高さ')),
                ('loudness', models.IntegerField(blank=True, default=1, null=True, verbose_name='音圧')),
                ('mode', models.IntegerField(blank=True, default=1, null=True, verbose_name='スケール')),
                ('speechiness', models.IntegerField(blank=True, default=1, null=True, verbose_name='話し言葉度')),
                ('acousticness', models.IntegerField(blank=True, default=1, null=True, verbose_name='アコースティック感')),
                ('instrumentalness', models.IntegerField(blank=True, default=1, null=True, verbose_name='ボーカル無し度')),
                ('liveness', models.IntegerField(blank=True, default=1, null=True, verbose_name='ライブ感')),
                ('valence', models.IntegerField(blank=True, default=1, null=True, verbose_name='ポジティブ')),
                ('tempo', models.IntegerField(blank=True, default=1, null=True, verbose_name='テンポ')),
                ('type', models.IntegerField(blank=True, default=1, null=True, verbose_name='タイプ')),
                ('url', models.IntegerField(blank=True, default=1, null=True, verbose_name='URL')),
            ],
        ),
        migrations.RemoveField(
            model_name='music_by_feeling',
            name='acousticness',
        ),
        migrations.RemoveField(
            model_name='music_by_feeling',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='music_by_feeling',
            name='danceability',
        ),
        migrations.RemoveField(
            model_name='music_by_feeling',
            name='energy',
        ),
        migrations.RemoveField(
            model_name='music_by_feeling',
            name='instrumentalness',
        ),
        migrations.RemoveField(
            model_name='music_by_feeling',
            name='key',
        ),
        migrations.RemoveField(
            model_name='music_by_feeling',
            name='liveness',
        ),
        migrations.RemoveField(
            model_name='music_by_feeling',
            name='loudness',
        ),
        migrations.RemoveField(
            model_name='music_by_feeling',
            name='mode',
        ),
        migrations.RemoveField(
            model_name='music_by_feeling',
            name='speechiness',
        ),
        migrations.RemoveField(
            model_name='music_by_feeling',
            name='tempo',
        ),
        migrations.RemoveField(
            model_name='music_by_feeling',
            name='type',
        ),
        migrations.RemoveField(
            model_name='music_by_feeling',
            name='url',
        ),
        migrations.RemoveField(
            model_name='music_by_feeling',
            name='valence',
        ),
        migrations.AlterField(
            model_name='music_by_feeling',
            name='title',
            field=models.CharField(max_length=50, null=True, verbose_name='タイトル'),
        ),
    ]
