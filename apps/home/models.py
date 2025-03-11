from django.db import models

from utils.model import DataTimeCreate


class Room(DataTimeCreate):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)


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

    def __str__(self):
        return f"{self.name} ({self.room})"
