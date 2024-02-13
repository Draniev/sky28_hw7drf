from rest_framework import viewsets, generics
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from .models import Course, Lesson, CourseSubscription
from .permissions import OwnerOrCheckDjangoPermissions
from .serializers import CourseSerializer, LessonSerializer, CourseSubscriptionSerializer


class Paginator(PageNumberPagination):
    page_size = 10  # Количество элементов на странице
    page_size_query_param = 'page_size'  # Параметр запроса для указания количества элементов на странице
    max_page_size = 100  # Максимальное количество элементов на странице


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (OwnerOrCheckDjangoPermissions, )
    pagination_class = Paginator

    def get_queryset(self):
        if self.request.user.groups.filter(name='Moderators').exists():
            # Allow moderators to view all courses
            return Course.objects.all()
        else:
            # Filter courses by owner for other users
            return Course.objects.filter(owner=self.request.user)
            # return Course.objects.all()


class LessonListCreateView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (OwnerOrCheckDjangoPermissions, )
    pagination_class = Paginator

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


class CourseSubscriptionCreateView(CreateAPIView):
    queryset = CourseSubscription.objects.all()
    serializer_class = CourseSubscriptionSerializer


class CourseSubscriptionDestroyView(DestroyAPIView):
    queryset = CourseSubscription.objects.all()
    serializer_class = CourseSubscriptionSerializer
    # permission_classes = [OwnerOrCheckDjangoPermissions]

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.filter(user=self.request.user, course_id=self.kwargs['course_id']).first()
        return obj