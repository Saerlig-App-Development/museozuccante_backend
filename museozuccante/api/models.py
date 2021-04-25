import uuid

from django.db import models


class Room(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=300)
    floor = models.IntegerField()
    number = models.IntegerField(default=0)
    pixel_x = models.DecimalField(decimal_places=5, max_digits=10, null=True, blank=True)
    pixel_y = models.DecimalField(decimal_places=5, max_digits=10, null=True, blank=True)

    def __str__(self):
        return self.title


class Company(models.Model):
    class Meta:
        verbose_name_plural = 'Companies'

    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=300)
    poster = models.URLField(max_length=300)
    still_active = models.BooleanField()
    body = models.TextField()

    def __str__(self):
        return self.title


class Item(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=300)
    poster = models.URLField(max_length=300)
    highlighted = models.BooleanField()
    body = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' ' + self.subtitle
