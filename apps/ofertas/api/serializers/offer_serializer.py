from rest_framework import serializers
from apps.ofertas.models import Offer


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation['image_first']:
            url = representation['image_first']
            url_image = url.split("&export=download")[0]
            representation['image_first'] = url_image
            return representation
        return representation
        