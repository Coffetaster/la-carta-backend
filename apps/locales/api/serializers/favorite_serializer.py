from datetime import date
from rest_framework import serializers
from apps.locales.models import Favorite, Local


class LocalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Local
        fields = ['id','visit','local_name','address','image','type','description']      

class FavoriteSerializer(serializers.ModelSerializer):
    local = LocalSerializer(read_only=True)
    
    class Meta:
        model = Favorite
        fields = ['local']
        