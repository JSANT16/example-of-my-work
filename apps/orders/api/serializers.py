from rest_framework import serializers
from apps.orders.models import Customer, Order
from apps.articles.api.serializers import ArticleSerializer


class CustumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('__all__')


class OrderSerializer(serializers.ModelSerializer):
    customer_details = CustumerSerializer()
    article_detail = ArticleSerializer()

    class Meta:
        model = Order
        fields = (
            'number',
            'customer',
            'customer_details',
            'delivered_date',
            'urgent',
            'warehouse',
            'reference',
            'store_code',
            'partner_code',
            'detail',
            'article',
            'article_detail',
            'quantity',
            'type_order'
        )
