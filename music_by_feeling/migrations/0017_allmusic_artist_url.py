# Generated by Django 2.1.5 on 2022-10-10 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_by_feeling', '0016_allmusic_genres'),
    ]

    operations = [
        migrations.AddField(
            model_name='allmusic',
            name='artist_url',
            field=models.CharField(max_length=100, null=True, verbose_name='アーティストURL'),
        ),
    ]
