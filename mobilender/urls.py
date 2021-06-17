from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenRefreshView
from .views import schema_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('mobilender.routes')),
    path('api/v1/token/refresh/', TokenRefreshView.as_view()),
    path('api/v1/docs/', schema_view.with_ui('swagger',
                                             cache_timeout=0), name='schema-swagger-ui'),
    re_path('^(?:.*)/?$', TemplateView.as_view(template_name="index.html")),

]
