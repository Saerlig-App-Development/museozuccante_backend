from django.contrib import admin

from .models import Room, Item, Company


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('title', 'subtitle', 'id')
    ordering = ('title',)
    search_fields = ('title', 'subtitle')


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    ordering = ('title',)
    list_display = ('title', 'floor', 'id')
    search_fields = ('title',)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    ordering = ('title',)
    list_display = ('title', 'id')
    search_fields = ('title',)
