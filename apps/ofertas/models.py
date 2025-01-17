from django.db import models
from apps.locales.models import Local
from apps.usuarios.models import User
from utils.validates.validates import validate_letters_numbers_and_spaces
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from utils.validates.validates import validate_digits,validate_alnum,validate_letters_and_spaces,validate_letters_numbers_and_spaces
from gdstorage.storage import GoogleDriveStorage

gd_storage = GoogleDriveStorage()

# Create your models here.
# Local
class Offer(models.Model):
    offer_description=models.TextField('Descripcion',max_length=100,default='AAA')
    offer_name = models.CharField('Nombre de la oferta',max_length=30, blank=False, null=False)
    local = models.ForeignKey(Local, on_delete=models.CASCADE,blank=False, null= False)
    min_date = models.DateField('Fecha inicial',blank=False, null= False)
    max_date = models.DateField('Fecha final',blank=False, null= False)
    image_first = models.ImageField('Imagen', upload_to='offer_image', storage=gd_storage, blank=True, null=True)
    
    # TODO: Define fields here

    class Meta:
        """Meta definition for Offer."""

        verbose_name = 'Oferta'
        verbose_name_plural = 'Ofertas'

    def __str__(self):
        """Unicode representation of Offer."""
        return f'{self.offer_name}'


class Promo(models.Model):
    promo_description=models.TextField('Descripcion',max_length=150,default='AAA',blank=False, null=False)
    promo_name = models.CharField('Nombre de la promo',max_length=30, blank=False, null=False)
    local = models.ForeignKey(Local, related_name='promoLocal', on_delete=models.CASCADE,blank=False, null= False)
    active=models.BooleanField(default=False)
    min_date = models.DateField('Fecha inicial',blank=False, null= False)
    max_date = models.DateField('Fecha final',blank=False, null= False)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Offer."""

        verbose_name = 'Promo'
        verbose_name_plural = 'Promos'

    def __str__(self):
        """Unicode representation of Promo."""
        return f'Promo {self.promo_name} del local {self.local}'
    
    def clean(self):
        # Verifica si existe otra promoción activa para el mismo local
        if self.active and Promo.objects.filter(local=self.local, active=True).exclude(pk=self.pk).exists():
            raise ValidationError("Ya existe una promoción activa para este local. No se puede tener más de una promoción activa.")



class Winer(models.Model):
    winer_name=models.CharField('Nombre', max_length=50,validators=[MinLengthValidator(3),validate_letters_and_spaces],blank=False, null=False)
    winer_ci = models.CharField('Carnet',validators=[MinLengthValidator(11),validate_digits], max_length=11, unique=False ,blank = False, null= False)
    winer_movil = models.CharField('Movil',validators=[MinLengthValidator(8),validate_digits], max_length=8, blank = False, null= False)
    promo = models.ForeignKey(Promo, on_delete=models.CASCADE,verbose_name='Promo',blank=False, null= False)
    
    # TODO: Define fields here

    class Meta:
        """Meta definition for Winer."""

        verbose_name = 'Ganador'
        verbose_name_plural = 'Ganadores'

    def __str__(self):
        """Unicode representation of Winer."""
        return f'Ganador {self.winer_name}: {self.promo}'

    def save(self, *args, **kwargs):
        super(Winer, self).save(*args, **kwargs)
