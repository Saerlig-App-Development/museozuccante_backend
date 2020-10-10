from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse

from .models import Item
from .serializer import serialize_item


def getAll(request: WSGIRequest):
    data = Item.objects.all()
    return JsonResponse(serialize_item(data), safe=False)


def getOne(request: WSGIRequest):
    return JsonResponse([], safe=False)
