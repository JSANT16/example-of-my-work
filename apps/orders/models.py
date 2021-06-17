from django.db import models
from apps.base.models import BaseModel
from apps.articles.models import Article

TYPE_CUSTUMER = (
    ('NORMAL', 'NORMAL'),
    ('SILVER', 'SILVER'),
    ('GOLD', 'GOLD'),
    ('PLATINUM', 'PLATINUM')
)


class Customer(BaseModel):

    name = models.CharField(max_length=230)
    code = models.CharField(max_length=100)
    pic = models.FileField(upload_to='customer-pic')
    address = models.CharField(max_length=250)
    type_custumer = models.CharField(
        max_length=8, choices=TYPE_CUSTUMER, default='NORMAL')


class Order(BaseModel):
    TYPE_ORDER = (
        ('DISTRIBUTION CENTER', 'DISTRIBUTION CENTER'),
        ('BRANCH', 'BRANCH'),
        ('ASSOCIATED COMPANY', 'ASSOCIATED COMPANY'),
    )
    number = models.PositiveIntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    delivered_date = models.DateTimeField()
    urgent = models.BooleanField(default=False)
    warehouse = models.CharField(blank=True, max_length=50)
    reference = models.CharField(blank=True, max_length=60)
    store_code = models.CharField(blank=True, max_length=30)
    partner_code = models.CharField(blank=True, max_length=30)
    detail = models.CharField(blank=True, max_length=70)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    type_order = models.CharField(
        choices=TYPE_ORDER, max_length=30, default='BRANCH')
