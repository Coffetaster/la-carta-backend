from rest_framework import serializers
from apps.locales.models import  Reviews


class ReviewsSerializer(serializers.ModelSerializer):
   
    
    class Meta:
        model = Reviews
        fields = ('id','user_name','description','active')
        
    
    
   
class CreateReviewsSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Reviews
        fields = '__all__'
        