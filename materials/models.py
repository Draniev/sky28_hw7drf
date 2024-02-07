from django.db import models


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.CharField(max_length=4096, verbose_name='Описание')
    avatar = models.ImageField(blank=True, null=True, upload_to='courses_avatars/')


class Lesson(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.CharField(max_length=4096, verbose_name='Описание')
    avatar = models.ImageField(blank=True, null=True, upload_to='lessons_avatars/')
    video = models.URLField(verbose_name='Видео')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
