from rest_framework.routers import DefaultRouter
from apps.articles.api.views import ArticleViewSet, VendorViewSet

router = DefaultRouter()

router.register('vendor', VendorViewSet)
router.register('article', ArticleViewSet, basename='article')
urlpatterns = router.urls
