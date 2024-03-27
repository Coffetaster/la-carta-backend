from django.db import models
from django.core.validators import MinLengthValidator,MinValueValidator
from apps.locales.models import Local
from utils.validates.validates import validate_digits, validate_letters_and_spaces,validate_letters_numbers_and_spaces

# Create your models here.

class Booking(models.Model):
    name = models.CharField('Nombre de la reserva',validators=[MinLengthValidator(3),validate_letters_numbers_and_spaces],default='Reserva' , max_length=50,blank=False, null=False)
    cost = models.DecimalField('Costo', max_digits=10,  decimal_places=2, blank= False, null= False)
    cant = models.PositiveIntegerField('Máximo de personas',default=1)
    active = models.BooleanField('Activo',default=True)
    local = models.ForeignKey(Local,on_delete=models.CASCADE,related_name='bookingLocal', verbose_name='Local',blank=False, null= False)
    
    class Meta:
        """Meta definition for Booking."""

        verbose_name = 'Reserva'
        verbose_name_plural = 'Receservaciones'

    def __str__(self):
        """Unicode representation of Booking."""
        return f'Reserva {self.id}'

class ClientBooking(models.Model):
    name = models.CharField('Nombre del usuario',validators=[MinLengthValidator(3),validate_letters_and_spaces], max_length=50,blank=False, null=False)
    cant= models.PositiveIntegerField('Cantidad de personas',validators=[MinValueValidator(1)], default=1, blank=False, null=False)
    ci=models.CharField('Carnet',validators=[MinLengthValidator(11),validate_digits], max_length=11, unique=False ,blank = False, null= False)
    movil =models.CharField('Movil',validators=[MinLengthValidator(8),validate_digits], max_length=8, blank = False, null= False)
    booking_active= models.BooleanField('Reservado',default=False)
    booking_date = models.DateField('Fecha',  null=False)
    booking_time = models.TimeField('Hora', null=False)
    booking = models.ForeignKey(Booking,on_delete=models.CASCADE, verbose_name='Reserva',blank=False, null= False)
    
    class Meta:
        """Meta definition for ClientBooking."""

        verbose_name = 'Reservación de cliente'
        verbose_name_plural = 'Reservaciones de clientes'

    def __str__(self):
        """Unicode representation of ClientBooking."""
        return f'{self.name}'