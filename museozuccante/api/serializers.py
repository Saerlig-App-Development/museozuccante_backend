from django.db.models import QuerySet
from django.forms import model_to_dict

from .models import Room, Item


def serialize_item(item: Item):
    data = model_to_dict(item)
    data['id'] = item.pk
    data['room'] = Room.objects.filter(pk=data['room']).values()[0]
    return data


def serialize_items(items: QuerySet):
    out = []
    for i in items:
        out.append(serialize_item(i))
    return out
