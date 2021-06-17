from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Mobilender API's Docs",
        default_version='v1',
        description="Docs of project",
        contact=openapi.Contact(email="jardm12@hotmail.com")
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
