# Generated by Django 2.2.28 on 2023-01-24 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_by_feeling', '0042_auto_20221225_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='artist',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='アーティストタイトル'),
        ),
    ]
