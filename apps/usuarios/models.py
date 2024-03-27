from django.db import models
from django.core.validators import MinLengthValidator
from utils.validates.validates import validate_digits,validate_alnum,validate_letters_and_spaces,validate_letters_and_spaces      
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as DjangoUserManager
from django.db import models

class UserManager(DjangoUserManager):
    def register_user(self, username, email, password):
        """
        Args:
            username: the username to use. must be unique.
            email: the email to use. must be unique.
            password: user password.

        Returns:
            user: user instance
        """

        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        return user

class User(AbstractUser):
    objects = UserManager()
    ci=models.CharField('Carnet',validators=[MinLengthValidator(11),validate_digits], max_length=11, unique=False ,blank = False, null= False)
    movil =models.CharField('Movil',validators=[MinLengthValidator(8),validate_digits], max_length=8, blank = False, null= False)
    first_name = models.CharField('Nombre', max_length=50,validators=[MinLengthValidator(3),validate_letters_and_spaces],blank=False, null=False)
    last_name = models.CharField('Apellidos',validators=[MinLengthValidator(3),validate_letters_and_spaces], max_length=50, blank=False, null=False)
    username = models.CharField('Username',validators=[MinLengthValidator(3),validate_alnum],max_length=50, unique=True,blank = False, null= False)
    email = models.EmailField('Email', max_length=50 , unique=True, blank = False, null= False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    
    class Meta:    
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        
    def __str__(self):
        return f'id:{self.id} {self.username}'
    
        