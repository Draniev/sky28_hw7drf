from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import Course, Lesson, CourseSubscription
from .validators import CheckVideoUrlValidator
from .tasks import notification_of_changes


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [CheckVideoUrlValidator(field='video'), ]


class CourseSerializer(serializers.ModelSerializer):
    lessons_qty = SerializerMethodField(read_only=True)
    lessons = LessonSerializer(read_only=True, many=True)
    subscribed = SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        course = Course.objects.create(owner=user, **validated_data)
        return course

    def save(self, **kwargs):
        course = super().save(**kwargs)
        if self.instance.pk:  # Check if instance exists (updated)
            notification_of_changes.delay(course)
        return course

    def get_lessons_qty(self, obj):
        return obj.lessons.count()

    def get_subscribed(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return CourseSubscription.objects.filter(user=request.user, course=obj).exists()
        return False


class CourseSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSubscription
        fields = '__all__'
        read_only_fields = ['user']

    def create(self, validated_data):
        user = self.context['request'].user
        subscription = CourseSubscription.objects.create(user=user, **validated_data)
        return subscription
