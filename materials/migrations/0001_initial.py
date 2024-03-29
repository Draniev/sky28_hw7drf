# Generated by Django 5.0.1 on 2024-01-28 18:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.CharField(max_length=4096, verbose_name='Описание')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='courses_avatars/')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.CharField(max_length=4096, verbose_name='Описание')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='lessons_avatars/')),
                ('video', models.URLField(verbose_name='Видео')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materials.course')),
            ],
        ),
    ]
