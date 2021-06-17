import django_filters as filters
from apps.orders.models import Order


class OrderFilter(filters.FilterSet):
    class Meta:
        model = Order
        fields = ['created', 'customer__id', 'delivered_date']
