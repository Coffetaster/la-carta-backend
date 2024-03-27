# Generated by Django 5.0.2 on 2024-02-24 18:22

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("locales", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="local",
            options={"verbose_name": "Local", "verbose_name_plural": "Locales"},
        ),
        migrations.CreateModel(
            name="Category",
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
                    "category_name",
                    models.CharField(
                        max_length=255, verbose_name="Nombre de la categoria"
                    ),
                ),
                (
                    "local",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="locales.local",
                        verbose_name="Local",
                    ),
                ),
            ],
            options={
                "verbose_name": "Categoria",
                "verbose_name_plural": "Categorias",
            },
        ),
        migrations.CreateModel(
            name="Gallery",
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
                    "local",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="locales.local",
                        verbose_name="Gallery",
                    ),
                ),
            ],
            options={
                "verbose_name": "Galeria de imagenes",
                "verbose_name_plural": "Galeria de imagenes",
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                    "product_name",
                    models.CharField(
                        max_length=255, verbose_name="Nombre del producto"
                    ),
                ),
                (
                    "cost",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Costo"
                    ),
                ),
                ("active", models.BooleanField(default=True)),
                (
                    "discount",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Descuento de %"
                    ),
                ),
                (
                    "stars",
                    models.PositiveSmallIntegerField(
                        default=5,
                        help_text="Number of stars between 1 and 5",
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ],
                        verbose_name="Estrellas",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="productCategory",
                        to="locales.category",
                        verbose_name="Category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Producto",
                "verbose_name_plural": "Productos",
            },
        ),
        migrations.CreateModel(
            name="Ingredient",
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
                    "ingredient_name",
                    models.CharField(
                        max_length=255, verbose_name="Nombre del ingrediente"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ingredientProduct",
                        to="locales.product",
                        verbose_name="Product",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ingrediente",
                "verbose_name_plural": "Ingredientes",
            },
        ),
        migrations.CreateModel(
            name="Aggregate",
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
                    "agregate_name",
                    models.CharField(
                        max_length=255, verbose_name="Nombre del agregado"
                    ),
                ),
                (
                    "measurement_unit",
                    models.CharField(max_length=50, verbose_name="Unidad de medida"),
                ),
                (
                    "measurement_unit_quantity",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        verbose_name="cantidad en unidades de medida",
                    ),
                ),
                (
                    "cost",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Costo"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="agregateProduct",
                        to="locales.product",
                        verbose_name="Product",
                    ),
                ),
            ],
            options={
                "verbose_name": "Agregado",
                "verbose_name_plural": "Agregados",
            },
        ),
    ]
