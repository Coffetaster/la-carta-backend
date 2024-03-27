# Generated by Django 5.0.2 on 2024-02-24 16:48

import django.core.validators
import django.utils.timezone
import utils.validates.validates
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "ci",
                    models.CharField(
                        max_length=11,
                        validators=[
                            django.core.validators.MinLengthValidator(11),
                            utils.validates.validates.validate_digits,
                        ],
                        verbose_name="Carnet",
                    ),
                ),
                (
                    "movil",
                    models.CharField(
                        max_length=8,
                        validators=[
                            django.core.validators.MinLengthValidator(8),
                            utils.validates.validates.validate_digits,
                        ],
                        verbose_name="Movil",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=50,
                        validators=[
                            django.core.validators.MinLengthValidator(3),
                            utils.validates.validates.validate_letters_and_spaces,
                        ],
                        verbose_name="Nombre",
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        max_length=50,
                        validators=[
                            django.core.validators.MinLengthValidator(3),
                            utils.validates.validates.validate_letters_and_spaces,
                        ],
                        verbose_name="Apellidos",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        max_length=50,
                        unique=True,
                        validators=[
                            django.core.validators.MinLengthValidator(3),
                            utils.validates.validates.validate_alnum,
                        ],
                        verbose_name="Username",
                    ),
                ),
                (
                    "email",
                    models.EmailField(max_length=50, unique=True, verbose_name="Email"),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Usuario",
                "verbose_name_plural": "Usuarios",
            },
        ),
    ]