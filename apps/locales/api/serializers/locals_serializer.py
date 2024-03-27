from datetime import date
from rest_framework import serializers
from apps.locales.api.serializers.local_detail_serializer import CategorySerializer, GallerySerializer
from apps.locales.api.serializers.reviews_serializers import ReviewsSerializer
from apps.locales.models import Local, Reviews
from apps.ofertas.api.serializers.promo_serializers import PromoSerializer
from apps.ofertas.models import Promo


class LocalSerializer(serializers.ModelSerializer):
    # reviewsLocal = serializers.SerializerMethodField()
    # galleryLocal = GallerySerializer(many=True, read_only=True)
    # categoryLocal = CategorySerializer(many=True, read_only=True)
    # promoLocal = serializers.SerializerMethodField()
    
    class Meta:
        model = Local
        fields = ('id', 'local_name', 'visit', 'type', 'address', 'image')
        # fields = ('id', 'local_name', 'visit', 'type', 'description', 'address', 'image', 'reviewsLocal', 'galleryLocal', 'categoryLocal', 'promoLocal')

  
    # def get_promoLocal(self, obj):
    #     today = date.today()
    #     active_promos = Promo.objects.filter(local=obj, active=True, min_date__lte=today, max_date__gte=today)
    #     return PromoSerializer(active_promos, many=True).data
    
    # def get_reviewsLocal(self, obj):
    #     active_reviews = Reviews.objects.filter(local=obj, active=True).order_by('-id')[:8]
    #     return ReviewsSerializer(active_reviews, many=True).data
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation['image']:
            url = representation['image']
            url_image = url.split("&export=download")[0]
            representation['image'] = url_image
            return representation
        return representation