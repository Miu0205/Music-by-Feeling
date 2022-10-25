# Generated by Django 2.1.5 on 2022-10-14 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_by_feeling', '0024_auto_20221014_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allmusic',
            name='track_id',
            field=models.CharField(max_length=100, null=True, verbose_name='track_id'),
        ),
        migrations.AlterField(
            model_name='favoritemusiclist',
            name='track_id',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='track_id'),
        ),
    ]
