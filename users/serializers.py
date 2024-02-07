from rest_framework import serializers

from materials.serializers import CourseSerializer, LessonSerializer
from users.models import Payment, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')


class PaymentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    course = CourseSerializer
    lesson = LessonSerializer

    class Meta:
        model = Payment
        fields = '__all__'
