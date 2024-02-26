from django.urls import path

from users.views import PaymentListView, UserApiView, PaymentCreateAPIView

urlpatterns = [
    path('payments/', PaymentListView.as_view(http_method_names=['get']), name='payment-list'),
    path('payments/create/', PaymentCreateAPIView.as_view(http_method_names=['post']), name='payment-create'),
    path('user/<int:pk>/', UserApiView.as_view(), name='user-api-view'),
]
