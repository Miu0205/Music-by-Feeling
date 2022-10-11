# Generated by Django 2.1.5 on 2022-09-12 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_by_feeling', '0003_music'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteMusicList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名前')),
                ('genres', models.CharField(max_length=50, verbose_name='ジャンル')),
                ('images', models.CharField(max_length=50, verbose_name='イメージ')),
                ('popularity', models.IntegerField(blank=True, default=1, null=True, verbose_name='人気度')),
                ('external_urls', models.CharField(max_length=50, verbose_name='外部URL')),
                ('uri', models.CharField(max_length=50, verbose_name='URI')),
                ('result1', models.CharField(max_length=50, verbose_name='結果1')),
            ],
        ),
        migrations.CreateModel(
            name='Music_by_feelingList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名前')),
                ('genres', models.CharField(max_length=50, verbose_name='ジャンル')),
                ('images', models.CharField(max_length=50, verbose_name='イメージ')),
                ('popularity', models.IntegerField(blank=True, default=1, null=True, verbose_name='人気度')),
                ('external_urls', models.CharField(max_length=50, verbose_name='外部URL')),
                ('uri', models.CharField(max_length=50, verbose_name='URI')),
                ('result1', models.CharField(max_length=50, verbose_name='結果1')),
            ],
        ),
    ]
