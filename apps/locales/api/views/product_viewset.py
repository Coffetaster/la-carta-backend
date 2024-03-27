from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from apps.locales.api.serializers.product_serializer import ProductDetailSerializer


class ProductDetailViewSet(viewsets.GenericViewSet):
    serializer_class= ProductDetailSerializer
    
    def get_queryset(self,pk=None):
        if pk:
            return self.get_serializer().Meta.model.objects.filter(active = True).filter(id = pk).first()
        return None
    
    def retrieve(self, request, pk = None):
        product = self.get_queryset(pk)
        if product:
            product_serializers = self.serializer_class(product)
            return Response(product_serializers.data, status= status.HTTP_200_OK)
        return Response({'message':'No existe el producto'}, status= status.HTTP_404_NOT_FOUND)
        