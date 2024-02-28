import re

from rest_framework.serializers import ValidationError


class CheckVideoUrlValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        video_url = dict(value).get(self.field)
        if video_url:
            x = re.search(r"^https://youtube.com/[A-Za-z0-9\=\?]+", video_url)
            if not x:
                raise ValidationError("Надо загружать с Ютуба!")
