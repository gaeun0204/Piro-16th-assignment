# Generated by Django 2.0.13 on 2022-01-14 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='releaseYear',
            field=models.CharField(default=1, max_length=10, verbose_name='개봉년도'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='runningTime',
            field=models.IntegerField(verbose_name='러닝타임'),
        ),
    ]
