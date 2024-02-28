from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.serializers import CourseSerializer, LessonSerializer
from users.models import Payment, User
from users.services import get_payment_link


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


class SimplePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        exclude = ('user',)


class UserIsOwnerViewSerializer(serializers.ModelSerializer):
    payments = SimplePaymentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'payments')


class UserNotOwnerViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name',)


class PaymentCreateSerializer(serializers.ModelSerializer):
    payment_link = SerializerMethodField(read_only=True)

    class Meta:
        model = Payment
        fields = ('course', 'lesson', 'amount', 'method', 'payment_link')

    def create(self, validated_data):
        user = self.context['request'].user
        payment = Payment.objects.create(user=user, **validated_data)
        return payment

    def get_payment_link(self, obj):
        if obj.method == Payment.PaymentMethod.BANK:
            return get_payment_link(obj)
        else:
            return None
