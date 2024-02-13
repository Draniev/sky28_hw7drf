from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


from materials.models import CourseSubscription, Course, Lesson
from users.models import User


class LessonCRUDTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@test.ru', password='password123'
        )
        self.course = Course.objects.create(
            name='Test Course', description='Test Description',
            owner=self.user,
        )
        self.lesson = Lesson.objects.create(
            name='Test lesson',
            description='Test lesson description',
            video='https://youtube.com/rsta',
            course=self.course,
            owner=self.user
        )

    def test_CR_lessons(self):
        client = APIClient()
        client.force_authenticate(user=self.user)

        test_data_1 = {
            'name': 'Test lesson 1',
            'description': 'Test lesson 1 description',
            'video': 'https://youtube.com/rsta',
            'course': self.course.id,
        }

        initial_count = Lesson.objects.count()
        response = client.post('/api/lessons/', data=test_data_1, format='json')
        new_count = Lesson.objects.count()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(new_count, initial_count + 1)

        test_data_2 = {
            'name': 'Test lesson 2',
            'description': 'Test lesson 2 description',
            'video': 'https://youtube.com/rsta',
            'course': self.course.id,
        }

        response = client.post('/api/lessons/', data=test_data_2, format='json')
        new_count = Lesson.objects.count()
        self.assertEqual(new_count, initial_count + 2)

        response = client.get('/api/lessons/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(f'response len {len(response.json().get("results"))} initial_count {initial_count}')
        self.assertEqual(len(response.json().get("results")), initial_count + 2)

    def test_partial_update_lessons(self):
        client = APIClient()
        client.force_authenticate(user=self.user)

        test_data = {
            'name': 'Updated Test lesson',
        }
        response = client.patch(f'/api/lessons/{self.lesson.id}/',
                                data=test_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = client.get(f'/api/lessons/{self.lesson.id}/')
        self.assertEqual(response.json().get("name"), 'Updated Test lesson')

    def test_update_lessons(self):
        client = APIClient()
        client.force_authenticate(user=self.user)

        test_data = {
            'name': 'Updated Test lesson',
            'description': 'Updated Test lesson description',
            'video': 'https://youtube.com/rsta',
            'course': self.course.id,
        }
        response = client.patch(f'/api/lessons/{self.lesson.id}/',
                                data=test_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = client.get(f'/api/lessons/{self.lesson.id}/')
        self.assertEqual(response.json().get("name"), 'Updated Test lesson')
        self.assertEqual(response.json().get("description"), 'Updated Test lesson description')

    def test_delete_lessons(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        initial_count = Lesson.objects.count()
        response = client.delete(f'/api/lessons/{self.lesson.id}/')
        new_count =  Lesson.objects.count()
        self.assertEqual(new_count, initial_count - 1)


class CourseSubscriptionTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@test.ru', password='password123'
        )
        self.course = Course.objects.create(
            name='Test Course', description='Test Description',
            owner=self.user,
        )

    def test_create_subscription(self):
        client = APIClient()
        client.force_authenticate(user=self.user)

        test_data = {
            'course': self.course.id,
        }

        initial_count = CourseSubscription.objects.count()
        response = client.post('/api/subscriptions/', data=test_data, format='json')
        new_count = CourseSubscription.objects.count()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(new_count, initial_count + 1)

    def test_delete_subscription(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        subscription = CourseSubscription.objects.create(user=self.user, course=self.course)

        initial_count = CourseSubscription.objects.count()
        response = client.delete(f'/api/subscriptions/{self.course.id}/')
        new_count = CourseSubscription.objects.count()

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(new_count, initial_count - 1)
