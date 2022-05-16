from django.db.models import QuerySet
from django.forms import model_to_dict

from .models import Room, Item, Company


def serialize_room(room: Room, full=True):
    data = model_to_dict(room)
    data['id'] = room.pk
    if full:
        data['items'] = serialize_items(Item.objects.filter(room_id=room.pk), room=False)
    return data


def serialize_company(company: Company, full=True):
    data = model_to_dict(company)
    data['id'] = company.pk
    if full:
        data['items'] = serialize_items(Item.objects.filter(company_id=company.pk), company=False)
    return data


def serialize_item(item: Item, room=True, company=True):
    data = model_to_dict(item)
    data['id'] = item.pk
    if room:
        data['room'] = serialize_room(Room.objects.get(pk=data['room']), full=False)
    if company:
        data['company'] = serialize_company(Company.objects.get(pk=data['company']), full=False)
    return data


def serialize_rooms(rooms: QuerySet):
    out = [serialize_room(r) for r in rooms]
    return out


def serialize_companies(companies: QuerySet):
    out = [serialize_company(c) for c in companies]
    return out


def serialize_items(items: QuerySet, room=True, company=True):
    out = [serialize_item(i, room=room, company=company) for i in items]
    return out
