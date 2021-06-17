from django.urls import path, include

urlpatterns = [
    path('articles/', include(('apps.articles.api.routers',
                               'articles'), namespace='articles')),
    path('orders/', include(('apps.orders.api.routers', 'orders'), namespace='orders')),
]
