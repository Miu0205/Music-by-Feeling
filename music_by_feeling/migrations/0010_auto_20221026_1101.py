# Generated by Django 2.2.28 on 2022-10-26 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music_by_feeling', '0009_auto_20221025_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music_by_feeling',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='music_by_feeling.Category'),
        ),
        migrations.AlterField(
            model_name='music_by_feeling',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='日付'),
        ),
        migrations.AlterField(
            model_name='music_by_feeling',
            name='title',
            field=models.CharField(max_length=50, null=True, verbose_name='タイトル'),
        ),
    ]
