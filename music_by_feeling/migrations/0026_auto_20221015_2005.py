# Generated by Django 2.1.5 on 2022-10-15 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_by_feeling', '0025_auto_20221014_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='allmusic',
            name='track_url',
            field=models.CharField(max_length=100, null=True, verbose_name='track_url'),
        ),
        migrations.AddField(
            model_name='favoritemusiclist',
            name='track_url',
            field=models.CharField(max_length=100, null=True, verbose_name='track_url'),
        ),
        migrations.AddField(
            model_name='music_by_feelinglist',
            name='track_url',
            field=models.CharField(max_length=100, null=True, verbose_name='track_url'),
        ),
    ]
