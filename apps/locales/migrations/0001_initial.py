# Generated by Django 5.0.2 on 2024-02-24 17:46

import django.core.validators
import django.db.models.deletion
import utils.validates.validates
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Local",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Restaurante", "Restaurante"),
                            ("Bar", "Bar"),
                            ("Cafeteria", "Cafeteria"),
                            ("Heladeria", "Heladeria"),
                            ("Pizzeria", "Pizzeria"),
                        ],
                        default="Restaurant",
                        max_length=15,
                        verbose_name="Tipo de local",
                    ),
                ),
                (
                    "local_name",
                    models.CharField(
                        max_length=255,
                        unique=True,
                        validators=[
                            django.core.validators.MinLengthValidator(3),
                            utils.validates.validates.validate_letters_numbers_and_spaces,
                        ],
                        verbose_name="Nombre del local",
                    ),
                ),
                ("active", models.BooleanField(default=True, verbose_name="Activo")),
                (
                    "address",
                    models.TextField(
                        default="calle 35 #4273 entre 46 y 48", verbose_name="Direccion"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]