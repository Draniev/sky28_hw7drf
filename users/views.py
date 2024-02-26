from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView

from users.models import Payment
from users.permissions import OwnerOrReadOnly
from users.serializers import PaymentSerializer, UserIsOwnerViewSerializer, UserNotOwnerViewSerializer, \
    PaymentCreateSerializer

User = get_user_model()


class PaymentListView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter,]
    ordering_fields = ('payment_date',)
    filterset_fields = ('course', 'lesson', 'method',)


class PaymentCreateAPIView(CreateAPIView):
    serializer_class = PaymentCreateSerializer


class UserApiView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserIsOwnerViewSerializer
    permission_classes = (OwnerOrReadOnly, )

    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        if self.request.user == self.get_object():
            # Если метод вызывает хозяин объекта
            serializer_class = self.get_serializer_class()
        else:
            serializer_class = UserNotOwnerViewSerializer
        kwargs.setdefault('context', self.get_serializer_context())
        return serializer_class(*args, **kwargs)