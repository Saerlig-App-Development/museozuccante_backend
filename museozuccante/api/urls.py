from django.urls import path

from .views import *

urlpatterns = [
    path('rooms/', getRooms),
    path('companies/', getCompanies),
    path('items/', getItems),
    path('room/<str:pk>/', getRoom),
    path('company/<str:pk>/', getCompany),
    path('item/<str:pk>/', getItem),
]
