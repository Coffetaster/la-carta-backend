from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from apps.ofertas.api.serializers.promo_serializers import PromoSerializer


class PromoViewSet(viewsets.GenericViewSet):
    serializer_class= PromoSerializer
    
    def get_queryset(self,pk=None):
        if pk:
            return self.get_serializer().Meta.model.objects.filter(id = pk).filter(active = True).first()
        return self.get_serializer().Meta.model.objects.filter(active = True)
    
    
    def list(self,request):
        offers = self.get_queryset()
        if offers.exists():
            offers_serializers = self.serializer_class(offers,many = True)
            return Response(offers_serializers.data, status = status.HTTP_200_OK)
        return Response({'message':'No existen promociones!'},status = status.HTTP_404_NOT_FOUND)
    
    def retrieve(self, request, pk = None):
        offer = self.get_queryset(pk)
        if offer:
            offer_serializers = self.serializer_class(offer)
            return Response(offer_serializers.data, status= status.HTTP_200_OK)
        return Response({'message':'No existe la promocion'}, status= status.HTTP_404_NOT_FOUND)

    
    