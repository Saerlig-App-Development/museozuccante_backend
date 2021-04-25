from django.db.models import QuerySet
from django.forms import model_to_dict

from .models import Room, Item, Company


def serialize_room(room: Room):
    data = model_to_dict(room)
    data['id'] = room.pk
    return data


def serialize_company(company: Company):
    data = model_to_dict(company)
    data['id'] = company.pk
    return data


def serialize_item(item: Item):
    data = model_to_dict(item)
    data['id'] = item.pk
    data['room'] = serialize_room(Room.objects.get(pk=data['room']))
    data['company'] = serialize_company(Company.objects.get(pk=data['company']))
    return data


def serialize_rooms(rooms: QuerySet):
    out = [serialize_room(r) for r in rooms]
    return out


def serialize_companies(companies: QuerySet):
    out = [serialize_company(c) for c in companies]
    return out


def serialize_items(items: QuerySet):
    out = [serialize_item(i) for i in items]
    return out
