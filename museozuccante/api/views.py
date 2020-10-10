from django.core.exceptions import ValidationError
from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse, HttpResponse

from .models import Item
from .serializers import serialize_item, serialize_items


def error(status):
    return HttpResponse(status=status)


def getAll(request: WSGIRequest):
    data = Item.objects.all()
    return JsonResponse(serialize_items(data), safe=False)


def getOne(request: WSGIRequest, pk):
    try:
        if len(Item.objects.filter(pk=pk)) == 0:
            raise ValidationError('Not found')
    except ValidationError:
        return error(404)
    return JsonResponse(serialize_item(Item.objects.get(pk=pk)), safe=False)
