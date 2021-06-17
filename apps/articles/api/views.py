from rest_framework import viewsets
from .serializers import VendorSerializer, ArticleSerializer


class VendorViewSet(viewsets.ModelViewSet):
    """
     API to work with vendors
    """
    queryset = VendorSerializer.Meta.model.objects.all()
    serializer_class = VendorSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """
     API to work with articles
    """
    queryset = ArticleSerializer.Meta.model.objects.all()
    serializer_class = ArticleSerializer
