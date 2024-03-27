from django.db import models
from apps.usuarios.models import User
from utils.validates.validates import validate_letters_numbers_and_spaces
from django.core.validators import MinLengthValidator,MinValueValidator,MaxValueValidator
from django.core.exceptions import ValidationError
from datetime import datetime
from gdstorage.storage import GoogleDriveStorage

gd_storage = GoogleDriveStorage()


# Create your models here.
# Local
class Local(models.Model):
    TYPE_CHOICES = [
        ('Restaurante', 'Restaurante'),
        ('Bar', 'Bar'),
        ('Cafeteria', 'Cafeteria'),
        ('Heladeria', 'Heladeria'),
        ('Pizzeria', 'Pizzeria'),

    ]
    description = models.TextField('Descricción del Local', default='Descricción del Local')
    visit = models.PositiveIntegerField('Visitado', default=0, blank=True, null=True)
    type = models.CharField('Tipo de local',max_length=15,default='Restaurant' ,choices=TYPE_CHOICES, blank=False, null=False)
    local_name = models.CharField('Nombre del local',validators=[MinLengthValidator(3),validate_letters_numbers_and_spaces], max_length=255, blank=False , null=False, unique=True)
    active = models.BooleanField('Activo', default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True,blank=False, null= False)
    address = models.TextField('Direccion',default='calle 35 #4273 entre 46 y 48',blank=False, null= False)
    image = models.ImageField('Dimenciones de imagen:(752x450)',upload_to='locals', storage=gd_storage, null=True)
    facebook = models.URLField(max_length=500,null=True,blank=True)
    instagram = models.URLField(max_length=500,null=True,blank=True)
    telegram = models.URLField(max_length=500,null=True,blank=True)
    whatsapp = models.URLField(max_length=500,null=True,blank=True)
    twitter = models.URLField(max_length=500,null=True,blank=True)
    # TODO: Define fields here
    
    class Meta:
        """Meta definition for Local."""

        verbose_name = 'Local'
        verbose_name_plural = 'Locales'

    def __str__(self):
        """Unicode representation of Local."""
        return f'{self.local_name}'
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.user = self.user
        super(Local, self).save(*args, **kwargs)
        
# Categories of Local
class Category(models.Model):
    
    category_name = models.CharField('Nombre de la categoria', max_length=255, blank=False , null=False)
    local = models.ForeignKey(Local,on_delete=models.CASCADE,related_name='categoryLocal', verbose_name='Local',blank=False, null= False)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        """Unicode representation of Category."""
        return self.category_name
    
# Product  
class Product(models.Model):
    """Model definition for Product."""
    
    product_name = models.CharField('Nombre del producto', max_length=255, blank=False , null=False)
    cost = models.DecimalField('Costo', max_digits=10,  decimal_places=2, blank= False, null= False)
    active = models.BooleanField(default=True)
    discount = models.PositiveIntegerField('Descuento de %', default=0, blank=False, null=False)
    image = models.ImageField('Dimenciones de imagen:(752x450)', upload_to='product_image', storage=gd_storage, blank=True, null=True)
    category = models.ForeignKey(Category,related_name='productCategory', on_delete=models.CASCADE, verbose_name='Category',blank=False, null= False)
    # Define fields here

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.product_name
    
    
    

class Aggregate(models.Model):
    """Model definition for Aggregate."""
    agregate_name = models.CharField('Nombre del agregado', max_length=255, blank=False , null=False)
    measurement_unit = models.CharField('Unidad de medida', max_length=50, blank=False , null=False)
    measurement_unit_quantity = models.DecimalField('cantidad en unidades de medida', max_digits=10,  decimal_places=2, blank= False, null= False)
    cost = models.DecimalField('Costo', max_digits=10,  decimal_places=2, blank= False, null= False)
    product = models.ForeignKey(Product,related_name='agregateProduct', on_delete=models.CASCADE, verbose_name='Product',blank=False, null= False)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Aggregate."""

        verbose_name = 'Agregado'
        verbose_name_plural = 'Agregados'

    def __str__(self):
        return f'id:{self.id} {self.agregate_name}. id:{self.product.id} Product {self.product.product_name}'


class Ingredient(models.Model):
    """Model definition for Ingredient."""
    ingredient_name = models.CharField('Nombre del ingrediente', max_length=255, blank=False , null=False)
    measurement_unit = models.CharField('Unidad de medida',default='unidades', max_length=50, blank=False , null=False)
    measurement_unit_quantity = models.DecimalField('cantidad en unidades de medida',default=4, max_digits=10,  decimal_places=2, blank= False, null= False)
    product = models.ForeignKey(Product,related_name='ingredientProduct', on_delete=models.CASCADE, verbose_name='Product',blank=False, null= False)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Ingredient."""

        verbose_name = 'Ingrediente'
        verbose_name_plural = 'Ingredientes'

    def __str__(self):
        return self.ingredient_name


class Gallery(models.Model):
    """Model definition for Gallery."""
    image = models.ImageField('Dimenciones de imagen:(640x540)', upload_to='local_gallery_image', storage=gd_storage, blank=False, null=False)
    local = models.ForeignKey(Local, on_delete=models.CASCADE, related_name='galleryLocal',verbose_name='Local',blank=False, null= False)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Gallery."""

        verbose_name = 'Galeria de imagenes'
        verbose_name_plural = 'Galeria de imagenes'

    def __str__(self):
        return f'Photo {self.id} of local {self.local.local_name}'


class Favorite(models.Model):
    """Model definition for Favorite."""
    active = models.BooleanField(default=False)
    local = models.ForeignKey(Local, on_delete=models.CASCADE, related_name='favoriteLocal',verbose_name='Local',blank=False, null= False)
    date = models.DateField('Fecha', auto_now_add=True, null=True)
    time = models.TimeField('Hora', auto_now_add=True, null=True)
    
    # TODO: Define fields here

    class Meta:
        """Meta definition for Favorite."""

        verbose_name = 'Local Faborito'
        verbose_name_plural = 'Locales Favoritos'

    def __str__(self):
        return f'{self.local.local_name}'
    
    def save(self, *args, **kwargs):
        self.date= datetime.today()
        self.time = datetime.now()
        super(Favorite, self).save(*args, **kwargs)
    
    
class Reviews(models.Model):
    user_name=models.CharField('Nombre del usuario', max_length=50,blank=False, null=False)
    description = models.TextField('Reseña', default='Me encanta el servicio que brindan')
    local = models.ForeignKey(Local, on_delete=models.CASCADE,related_name='reviewsLocal',verbose_name='Local',blank=False, null= False)
    active = models.BooleanField(default=True)
    
    # TODO: Define fields here

    class Meta:
        """Meta definition for Reviews."""

        verbose_name = 'Reseña'
        verbose_name_plural = 'Reseñas'