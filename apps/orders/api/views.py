from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CustumerSerializer, OrderSerializer
from apps.orders.api.filters import OrderFilter


class CustumerViewSet(viewsets.ModelViewSet):
    """
    API to work with custumers
    """
    queryset = CustumerSerializer.Meta.model.objects.all()
    serializer_class = CustumerSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    API to work with orders
    """
    queryset = OrderSerializer.Meta.model.objects.all()
    serializer_class = OrderSerializer
    filter_class = OrderFilter


@api_view(['GET'])
def dashboard(request, *args, **kwargs):
    """
    ENDPOINT TO GET SOME REPORTS TO DASHBOARD
    """
    return Response(status=204)
