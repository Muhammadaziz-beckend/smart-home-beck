from django.db import models


class DataTimeCreate(models.Model):
    dt_create = models.DateTimeField("Дата создания", auto_now_add=True)
    dt_update = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        abstract = True
