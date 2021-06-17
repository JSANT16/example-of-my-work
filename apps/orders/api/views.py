from django.db.models import Count
from rest_framework import viewsets, status
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
    ---
        response 200Ok:
            - response:
            {
            'total_orders': int,
            'total_orders_by_type': [{type_order:int}],
            'total_urgent': int
        }
    """
    try:
        total_orders = OrderSerializer.Meta.model.objects.count()
        total_orders_by_type = OrderSerializer.Meta.model.objects.all().values(
            'type_order').annotate(total=Count('type_order')).order_by('total')
        total_urgent = OrderSerializer.Meta.model.objects.filter(
            urgent=True).count()
        data = {
            'total_orders': total_orders,
            'total_orders_by_type': total_orders_by_type,
            'total_urgent': total_urgent
        }
        return Response(data, status=status.HTTP_200_OK)
    except:
        return Response({'message': 'Somthing wrong'}, status.HTTP_400_BAD_REQUEST)
