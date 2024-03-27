from rest_framework.routers import DefaultRouter
from apps.reservas.api.views.booking_viewset import ClienteBookingViewSet




router = DefaultRouter()
router.register(r'create',ClienteBookingViewSet, basename = 'create'),



urlpatterns = router.urls 