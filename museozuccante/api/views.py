from django.core.exceptions import ValidationError
from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse, HttpResponse

from .models import Item, Room
from .serializers import *


def http_error(status):
    return HttpResponse(status=status)


def getRooms(request: WSGIRequest):
    data = Room.objects.all()
    return JsonResponse(serialize_rooms(data), safe=False)


def getItems(request: WSGIRequest):
    data = Item.objects.all()
    return JsonResponse(serialize_items(data), safe=False)


def getRoom(request: WSGIRequest, pk):
    try:
        if len(Room.objects.filter(pk=pk)) == 0:
            raise ValidationError('Not found')
    except ValidationError:
        return http_error(404)
    return JsonResponse(serialize_room(Room.objects.get(pk=pk)), safe=False)


def getItem(request: WSGIRequest, pk):
    try:
        if len(Item.objects.filter(pk=pk)) == 0:
            raise ValidationError('Not found')
    except ValidationError:
        return http_error(404)
    return JsonResponse(serialize_item(Item.objects.get(pk=pk)), safe=False)
