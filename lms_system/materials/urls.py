from django.urls import path, include
from rest_framework import routers

from .views import CourseViewSet, LessonListCreateView, LessonRetrieveUpdateDestroyView

router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('lessons/', LessonListCreateView.as_view(), name='lesson-list-create'),
    path('lessons/<int:pk>/', LessonRetrieveUpdateDestroyView.as_view(), name='lesson-retrieve-update-destroy'),
    path('', include(router.urls)),
]
