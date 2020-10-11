from django.urls import path

from .views import *

urlpatterns = [
    path('rooms/', getRooms),
    path('items/', getItems),
    path('item/<str:pk>', getItem),
    path('room/<str:pk>', getRoom),
]
