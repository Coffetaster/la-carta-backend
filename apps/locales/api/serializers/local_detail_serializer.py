from rest_framework import serializers
from apps.locales.api.serializers.product_serializer import ProductSerializer
from apps.locales.models import Category, Gallery,Local, Reviews
from apps.ofertas.api.serializers.promo_serializers import PromoSerializer
from apps.ofertas.models import Promo
from datetime import date
from apps.locales.api.serializers.reviews_serializers import ReviewsSerializer
from apps.reservas.models import Booking
from apps.reservas.api.serializers.booking_serializers import BookingSerializer


class CategorySerializer(serializers.ModelSerializer):
    productCategory = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('id','category_name','productCategory')

class GallerySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Gallery
        fields = ('id','image')
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation['image']:
            url = representation['image']
            url_image = url.split("&export=download")[0]
            representation['image'] = url_image
            return representation
        return representation

class LocalDetailSerializer(serializers.ModelSerializer):
    bookingLocal = serializers.SerializerMethodField()
    reviewsLocal = serializers.SerializerMethodField()
    galleryLocal = GallerySerializer(many=True, read_only=True)
    categoryLocal = CategorySerializer(many=True, read_only=True)
    promoLocal = serializers.SerializerMethodField()
    isAsequible = serializers.SerializerMethodField()
    
    class Meta:
        model = Local
        fields = ('id','facebook','instagram','telegram','whatsapp','twitter', 'local_name', 'visit', 'type', 'description', 'address', 'image','bookingLocal', 'reviewsLocal', 'galleryLocal', 'categoryLocal', 'promoLocal','isAsequible')

    def get_promoLocal(self, obj):
        today = date.today()
        active_promos = Promo.objects.filter(local=obj, active=True, min_date__lte=today, max_date__gte=today)
        return PromoSerializer(active_promos, many=True).data
    
    def get_reviewsLocal(self, obj):
        active_reviews = Reviews.objects.filter(local=obj, active=True).order_by('-id')[:8]
        return ReviewsSerializer(active_reviews, many=True).data
    
    def get_isAsequible(self, obj):
        # Verifica si el usuario asociado con el local pertenece al grupo "asegurable"
        return obj.user.groups.filter(name='asequible').exists()
    
    def get_bookingLocal(self, obj):
        booking = Booking.objects.filter(local = obj , active = True)
        return BookingSerializer(booking, many = True).data
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation['image']:
            url = representation['image']
            url_image = url.split("&export=download")[0]
            representation['image'] = url_image
            return representation
        return representation