# Generated by Django 2.1.5 on 2023-01-25 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_by_feeling', '0046_remove_allmusic_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music_by_feeling_selection_history',
            name='artist',
        ),
    ]