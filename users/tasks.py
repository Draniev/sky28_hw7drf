from django.utils import timezone

from config import celery_app
from users.models import User


def check_user_last_visit(user: User) -> None:
    last_login = user.last_login
    current_time = timezone.now()

    # Проверка, не заходил ли пользователь более месяца
    if current_time - last_login > timezone.timedelta(days=30):
        user.is_active = False
        user.save()


@celery_app.task()
def check_users() -> None:
    users = User.objects.all()
    for user in users:
        check_user_last_visit.delay(user)
