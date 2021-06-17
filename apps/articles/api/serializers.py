from rest_framework import serializers
from apps.articles.models import Article, Vendor


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('__all__')


class ArticleSerializer(serializers.ModelSerializer):
    vendors_detail = VendorSerializer(
        source='vendors', many=True, read_only=True)

    class Meta:
        model = Article
        fields = (
            'id',
            'code',
            'description',
            'price',
            'vendors',
            'vendors_detail',
            'created'
        )
