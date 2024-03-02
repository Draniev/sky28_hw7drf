from config import celery_app
from django.conf import settings
from django.core.mail import send_mail

from materials.models import Course, CourseSubscription


@celery_app.task()
def notification_of_changes(course: Course) -> None:
    subject = 'Изменился курс, на который вы подписаны'
    body = f'В курсе {course.name} произошли изменения.'
    from_email = settings.DEFAULT_FROM_EMAIL

    subscribers = CourseSubscription.objects.filter(course=course)
    recipient_list = [subscriber.user.email for subscriber in subscribers]

    send_mail(subject, body, from_email, recipient_list)