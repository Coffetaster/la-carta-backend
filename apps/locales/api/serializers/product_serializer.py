from rest_framework import serializers
from apps.locales.models import Aggregate, Ingredient, Product


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ('id','product_name','cost','discount','image','category_name')
        
    def get_category_name(self, obj):
        return obj.category.category_name
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation['image']:
            url = representation['image']
            url_image = url.split("&export=download")[0]
            representation['image'] = url_image
            return representation
        return representation

class AggregateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aggregate
        fields = ('id','agregate_name','measurement_unit','measurement_unit_quantity','cost')


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id','ingredient_name','measurement_unit','measurement_unit_quantity')


class ProductDetailSerializer(serializers.ModelSerializer):
    agregateProduct = AggregateSerializer(many=True, read_only=True)
    ingredientProduct = IngredientSerializer(many=True, read_only=True)
    category_name = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ('id','product_name','cost','discount','category_name','image','agregateProduct','ingredientProduct')


    def get_category_name(self, obj):
        return obj.category.category_name
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation['image']:
            url = representation['image']
            url_image = url.split("&export=download")[0]
            representation['image'] = url_image
            return representation
        return representation