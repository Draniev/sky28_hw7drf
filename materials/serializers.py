from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import Course, Lesson
from .validators import CheckVideoUrlValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [CheckVideoUrlValidator(field='video'), ]


class CourseSerializer(serializers.ModelSerializer):
    lessons_qty = SerializerMethodField(read_only=True)
    lessons = LessonSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons_qty(self, obj):
        return obj.lessons.count()
