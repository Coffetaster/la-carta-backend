from datetime import date
from rest_framework import serializers
from apps.reservas.models import Booking, ClientBooking
from django.core.exceptions import ValidationError

class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = '__all__'
        
        
class ClienteBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientBooking
        fields= ['name','cant','ci','movil','booking_date','booking_time','booking']
        
    def validate(self, data):
        # Retrieve the 'cant' value from the submitted data
        client_cant = data.get('cant')
        # Retrieve the 'booking' ForeignKey instance
        booking_instance = data.get('booking')

        # Check if the booking instance exists and has a 'cant' attribute
        if booking_instance and hasattr(booking_instance, 'cant'):
            # Compare the 'cant' value from the submitted data with the 'cant' value from the booking instance
            if client_cant > booking_instance.cant:
                raise ValidationError({
                    'cant': "El numero de personas exede la cantidad permitida."
                })

        # Always return the validated data
        return data