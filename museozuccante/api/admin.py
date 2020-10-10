from django.contrib import admin

from .models import Room, Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')
    ordering = ('title',)
    search_fields = ('title', 'subtitle')


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass
