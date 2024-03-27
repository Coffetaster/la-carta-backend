from rest_framework import serializers
from apps.ofertas.models import Offer, Promo


class PromoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promo
        fields = '__all__'
        