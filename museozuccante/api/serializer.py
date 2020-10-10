from django.conf import settings
from django.db.models import QuerySet

from .models import Room


def serialize_item(items: QuerySet):
    data = list(items.values())
    print(type(data))
    for d in data:
        if isinstance(d, dict):
            print(d['body'])
            with open(settings.MEDIA_ROOT + d['body'], 'r') as f:
                d['body'] = f.readlines()
            d['room'] = Room.objects.filter(pk=d['room_id']).values()[0]
            d.pop('room_id')
    return data
