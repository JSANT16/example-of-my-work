from django.urls import path, include

urlpatterns = [
    path('articles/', include('apps.articles.api.routers')),
    path('orders/', include('apps.orders.api.routers')),
]
