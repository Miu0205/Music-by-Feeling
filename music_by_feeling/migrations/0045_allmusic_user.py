# Generated by Django 2.2.28 on 2023-01-25 03:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music_by_feeling', '0044_auto_20230125_0334'),
    ]

    operations = [
        migrations.AddField(
            model_name='allmusic',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
