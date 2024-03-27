from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from apps.reservas.api.serializers.booking_serializers import ClienteBookingSerializer


class ClienteBookingViewSet(viewsets.GenericViewSet):
    serializer_class= ClienteBookingSerializer
    
    def create(self,request):
        serializers = self.serializer_class(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'message':'Reserva creada'}, status = status.HTTP_201_CREATED)
        return Response(serializers.errors,status = status.HTTP_400_BAD_REQUEST)
        