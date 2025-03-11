from django.db import models
from django_resized import ResizedImageField

from utils.model import DataTimeCreate


class Room(DataTimeCreate):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Комната"
        verbose_name_plural = "Комнаты"

    def __str__(self):
        return self.name


class Category(models.Model):
    img = ResizedImageField(
        ("Изображения"),
        size=[500, 500],
        upload_to="category's/",
        force_format="WEBP",
        quality=90,
        null=True,
        blank=True,
    )
    name = models.CharField("Названия",max_length=100)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    
    def __str__(self):
        return self.name


class Device(DataTimeCreate):
    category = models.ForeignKey(
        "Category",
        models.CASCADE,
        related_name="devices",
        verbose_name="категория",
    )
    modbus_address = models.IntegerField(
        verbose_name="Адрес modbus'a",
    )
    status = models.BooleanField(
        "Статус устройства",
        default=False,
    )
    room = models.ForeignKey(
        Room,
        verbose_name="Комната",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Девайс"
        verbose_name_plural = "Девайсы"

    def __str__(self):
        return f"{self.category.name} ({self.room})"
