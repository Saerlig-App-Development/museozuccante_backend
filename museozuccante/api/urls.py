from django.urls import path

from .views import *

urlpatterns = [
    path('item/', getAll),
    path('item/<str:pk>', getOne)
]
