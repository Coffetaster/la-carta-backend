from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from apps.ofertas.api.serializers.winner_serializers import WinerSerializer
from apps.ofertas.models import Winer
from django.db.models import Q

class WinerViewSet(viewsets.GenericViewSet):
    serializer_class= WinerSerializer

    def get_queryset(self):
    
        return self.get_serializer().Meta.model.objects.all()
    
    
    def create(self,request):
        serializers = self.serializer_class(data = request.data)
        query = Q(promo=request.data['promo']) & (Q(winer_ci=request.data['winer_ci']) | Q(winer_movil=request.data['winer_movil']))
        winers = Winer.objects.filter(query).exists()
        if not winers:
            if serializers.is_valid():
                serializers.save()
                return Response({'message':'creado con exito'}, status = status.HTTP_201_CREATED)
            return Response({'error':'Compruebe que haya escrito bien los datos'},status = status.HTTP_400_BAD_REQUEST)
        return Response({'error':'Ya existe un usuario con esos datos'},status = status.HTTP_400_BAD_REQUEST)
        