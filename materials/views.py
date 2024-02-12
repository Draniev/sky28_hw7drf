from rest_framework import viewsets, generics

from .models import Course, Lesson
from .permissions import OwnerOrCheckDjangoPermissions
from .serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (OwnerOrCheckDjangoPermissions, )

    def get_queryset(self):
        if self.request.user.groups.filter(name='Moderators').exists():
            # Allow moderators to view all courses
            return Course.objects.all()
        else:
            # Filter courses by owner for other users
            return Course.objects.filter(owner=self.request.user)


class LessonListCreateView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (OwnerOrCheckDjangoPermissions, )

    def get_queryset(self):
        if self.request.user.groups.filter(name='moderator').exists():
            # Allow moderators to view all lessons
            return Lesson.objects.all()
        else:
            # Filter lessons by owner for other users
            return Lesson.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (OwnerOrCheckDjangoPermissions, )

    def get_queryset(self):
        if self.request.user.groups.filter(name='moderator').exists():
            # Allow moderators to view all lessons
            return Lesson.objects.all()
        else:
            # Filter lessons by owner for other users
            return Lesson.objects.filter(owner=self.request.user)