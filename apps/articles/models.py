from django.db import models
from apps.base.models import BaseModel


class Vendor(BaseModel):
    name = models.CharField(max_length=230)
    address = models.CharField(max_length=250)


class Article(BaseModel):
    code = models.PositiveIntegerField()
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    vendors = models.ManyToManyField(Vendor)
