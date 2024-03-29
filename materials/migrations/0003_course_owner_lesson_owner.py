# Generated by Django 5.0.1 on 2024-02-12 20:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_alter_lesson_course'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='courses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='lesson',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='lessons', to=settings.AUTH_USER_MODEL),
        ),
    ]
