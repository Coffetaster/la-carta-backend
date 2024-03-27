from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from apps.locales.api.serializers.locals_serializer import LocalSerializer
from apps.locales.api.serializers.local_detail_serializer import LocalDetailSerializer
from apps.locales.models import Local, Reviews


class LocalsViewSet(viewsets.GenericViewSet):
    serializer_class= LocalSerializer
    
    def get_queryset(self,pk=None):
        if pk:
            return self.get_serializer().Meta.model.objects.filter(active = True).filter(id = pk).first()
        return self.get_serializer().Meta.model.objects.filter(active = True)
    
    def list(self,request):
        locals = self.get_queryset()
        if locals.exists():
            locals_serializers = self.serializer_class(locals,many = True)
            return Response(locals_serializers.data, status = status.HTTP_200_OK)
        return Response({'message':'No existen locales!'},status = status.HTTP_404_NOT_FOUND)
    
    def retrieve(self, request, pk = None):
        local = self.get_queryset(pk)
        if local:
            local.visit+=1
            local.save()
            local_serializers = LocalDetailSerializer(local)
            return Response(local_serializers.data, status= status.HTTP_200_OK)
        return Response({'message':'No existe el local'}, status= status.HTTP_404_NOT_FOUND)

class LocalsTypeViewSet(viewsets.GenericViewSet):
    serializer_class= LocalSerializer
    
    def get_queryset(self,pk=None):
        if pk:
            return self.get_serializer().Meta.model.objects.filter(active = True).filter(type = pk)
        return None
    
    
    def retrieve(self, request, pk = None):
        local = self.get_queryset(pk)
        if local.exists():
            local_serializers = LocalDetailSerializer(local,many=True)
            return Response(local_serializers.data, status= status.HTTP_200_OK)
        return Response({'message':'No existe locales'}, status= status.HTTP_404_NOT_FOUND)