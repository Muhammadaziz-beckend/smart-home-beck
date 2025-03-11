from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.safestring import mark_safe

from .models import *


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "dt_create",
        "dt_update",
    )

    list_display_links = (
        "id",
        "name",
        "dt_create",
        "dt_update",
    )

    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        "get_img",
        "id",
        "name",
    )

    list_display_links = (
        "get_img",
        "id",
        "name",
    )

    search_fields = ("name",)

    @admin.display(description=("Изображения"))
    def get_img(self, category: Category):
        if category.img:
            return mark_safe(
                f'<img src="{category.img.url}" alt="{category.name}" width="100px" />'
            )
        return "-"


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "category",
        "modbus_address",
        "status",
        "room",
        "dt_create",
        "dt_update",
    )

    list_display_links = (
        "id",
        "category",
        "modbus_address",
        "dt_create",
        "dt_update",
    )

    list_editable = (
        "status",
        "room",
    )

    list_filter = (
        "status",
        "dt_create",
        "dt_update",
        "category",
        "room",
    )
