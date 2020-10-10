import os
import uuid

from api.validators import validate_md
from django.conf import settings
from django.db import models


def get_unique_filename(instance, filename):
    ext = filename.split('.')[-1].lower()
    return os.path.join(settings.MARKDOWN_DIR, f'{uuid.uuid4()}.{ext}')


class Room(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=300)
    floor = models.IntegerField()
    number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


class Item(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=300)
    poster = models.URLField(max_length=300)
    body = models.FileField(upload_to=get_unique_filename, validators=[validate_md])
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' ' + self.subtitle
