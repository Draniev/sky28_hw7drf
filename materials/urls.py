from django.urls import path, include
from rest_framework import routers

from .views import CourseViewSet, LessonListCreateView, LessonRetrieveUpdateDestroyView, CourseSubscriptionCreateView, \
    CourseSubscriptionDestroyView

router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('lessons/', LessonListCreateView.as_view(), name='lesson-list-create'),
    path('lessons/<int:pk>/', LessonRetrieveUpdateDestroyView.as_view(), name='lesson-retrieve-update-destroy'),
    path('', include(router.urls)),
    path('subscriptions/', CourseSubscriptionCreateView.as_view(),
         name='create-course-subscription'),
    path('subscriptions/<int:course_id>/', CourseSubscriptionDestroyView.as_view(),
         name='remove-course-subscription'),
]
