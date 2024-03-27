from rest_framework import serializers
from apps.ofertas.models import Winer


class WinerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Winer
        fields = '__all__'
        