from rest_framework.routers import DefaultRouter
from apps.locales.api.views.locals_viewset import LocalsTypeViewSet, LocalsViewSet
from apps.locales.api.views.product_viewset import ProductDetailViewSet
from apps.locales.api.views.reviews_viewset import ReviewsViewSet



router = DefaultRouter()
router.register(r'list',LocalsViewSet, basename = 'list'),
router.register(r'product',ProductDetailViewSet, basename = 'product'),
router.register(r'type',LocalsTypeViewSet, basename = 'type'),
router.register(r'reviews',ReviewsViewSet, basename = 'reviews'),


urlpatterns = router.urls 