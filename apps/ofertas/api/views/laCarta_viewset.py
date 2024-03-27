from datetime import date
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from apps.ofertas.api.serializers.promo_serializers import PromoSerializer
from apps.ofertas.api.serializers.offer_serializer import OfferSerializer
from apps.ofertas.models import Offer
from apps.locales.models import Favorite, Local
from apps.locales.api.serializers.locals_serializer import LocalSerializer
from apps.locales.api.serializers.favorite_serializer import FavoriteSerializer
from rest_framework.exceptions import APIException

class LaCartaViewSet(viewsets.GenericViewSet):
    
    
    def list(self,request):
        try:
            offers = Offer.objects.filter(min_date__lte=date.today(), max_date__gte=date.today())
            locals = Local.objects.filter(active = True)
            favorites = Favorite.objects.filter(active = True)
            locals_serializers = LocalSerializer(locals,many=True)
            favorites_serializers = FavoriteSerializer(favorites,many=True)
            offers_serializers = OfferSerializer(offers,many = True)
            return Response({'favorites':favorites_serializers.data,'local':locals_serializers.data,'offer':offers_serializers.data},  status = status.HTTP_200_OK)
        except Exception as e:
            raise APIException("Error interno del servidor. Por favor, inténtalo de nuevo más tarde.", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)