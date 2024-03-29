# Generated by Django 2.1.5 on 2022-12-25 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_by_feeling', '0041_auto_20221225_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='dance_down',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='踊りやすさダウン'),
        ),
        migrations.AddField(
            model_name='history',
            name='dance_up',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='踊りやすさアップ'),
        ),
        migrations.AddField(
            model_name='history',
            name='energy_down',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='エネルギッシュダウン'),
        ),
        migrations.AddField(
            model_name='history',
            name='energy_up',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='エネルギッシュアップ'),
        ),
        migrations.AddField(
            model_name='history',
            name='image_url',
            field=models.CharField(max_length=100, null=True, verbose_name='イメージURL'),
        ),
    ]
