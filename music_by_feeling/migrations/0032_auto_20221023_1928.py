# Generated by Django 2.1.5 on 2022-10-23 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_by_feeling', '0031_auto_20221023_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='allmusic',
            name='rank',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='順位'),
        ),
        migrations.AddField(
            model_name='favoritemusiclist',
            name='rank',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='順位'),
        ),
        migrations.AddField(
            model_name='music_by_feelinglist',
            name='rank',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='順位'),
        ),
    ]