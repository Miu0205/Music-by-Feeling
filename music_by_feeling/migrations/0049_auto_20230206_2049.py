# Generated by Django 2.1.5 on 2023-02-06 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_by_feeling', '0048_auto_20230125_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='artist',
            field=models.CharField(max_length=50, null=True, verbose_name='アーティストタイトル'),
        ),
        migrations.AlterField(
            model_name='music',
            name='era',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='年代'),
        ),
    ]
