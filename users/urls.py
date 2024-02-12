from django.urls import path

from users.views import PaymentListView, UserApiView

urlpatterns = [
    path('payments/', PaymentListView.as_view(), name='payment-list'),
    path('user/<int:pk>/', UserApiView.as_view(), name='user-api-view'),
]
