# Generated by Django 2.2.28 on 2023-01-26 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_by_feeling', '0047_auto_20230125_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='artist',
            field=models.CharField(blank=True, default='5', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='music_by_feeling_selection_history',
            name='artist',
            field=models.CharField(max_length=50, null=True, verbose_name='アーティスト名'),
        ),
        migrations.AlterField(
            model_name='history',
            name='artist',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='アーティストタイトル'),
        ),
    ]
