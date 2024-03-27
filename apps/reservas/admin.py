from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['pk', 'cost','active','local']
    list_per_page = 10

    
    
    def get_queryset(self, request):
        # Obtén el queryset original
        qs = super().get_queryset(request)
        
        if request.user.is_superuser:
            return qs
        else: 
            return qs.filter(local__user=request.user)
        
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "local":
            kwargs["queryset"] = Local.objects.filter(user=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)   
        
@admin.register(ClientBooking)
class ClientBookingAdmin(admin.ModelAdmin):
    list_display = [ 'name','ci','movil','cant','booking_active','booking']
    list_per_page = 10

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "booking":
            kwargs["queryset"] = Booking.objects.filter(local__user=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)   
    
    def get_queryset(self, request):
        # Obtén el queryset original
        qs = super().get_queryset(request)
        
        if request.user.is_superuser:
            return qs
        else: 
            return qs.filter(booking__local__user=request.user)