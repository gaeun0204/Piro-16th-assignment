# Generated by Django 3.1.3 on 2022-01-19 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devtool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='이름')),
                ('kind', models.CharField(max_length=50, verbose_name='종류')),
                ('description', models.TextField(verbose_name='개발툴설명')),
            ],
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='아이디어명')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image', verbose_name='대표사진')),
                ('content', models.TextField(verbose_name='아이디어설명')),
                ('interest', models.IntegerField(verbose_name='아이디어관심도')),
                ('devtool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swidea.devtool')),
            ],
        ),
    ]
