from django.urls.conf import path
from rest_framework.routers import DefaultRouter
from apps.orders.api.views import CustumerViewSet, OrderViewSet, dashboard

router = DefaultRouter()

router.register('custumer', CustumerViewSet)
router.register('order', OrderViewSet)
urlpatterns = [
    path('dashboad/', dashboard, name='dashboard')
] + router.urls
