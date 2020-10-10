from django.urls import path

from .views import getAll

urlpatterns = [
    path('all/', getAll)
]
