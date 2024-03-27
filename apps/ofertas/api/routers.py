from rest_framework.routers import DefaultRouter
from apps.ofertas.api.views.promo_viewset import PromoViewSet
from apps.ofertas.api.views.laCarta_viewset import LaCartaViewSet
from apps.ofertas.api.views.winer_viewset import WinerViewSet



router = DefaultRouter()
router.register(r'winer',WinerViewSet, basename = 'winer'),
router.register(r'detail',PromoViewSet, basename = 'detail'),
router.register(r'laCarta',LaCartaViewSet, basename = 'laCarta'),

urlpatterns = router.urls 