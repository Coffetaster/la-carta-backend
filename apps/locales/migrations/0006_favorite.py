# Generated by Django 5.0.2 on 2024-03-03 12:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("locales", "0005_local_visit_product_visit_alter_category_local_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Favorite",
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
                ("active", models.BooleanField(default=False)),
                (
                    "local",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="favoriteLocal",
                        to="locales.local",
                        verbose_name="Local",
                    ),
                ),
            ],
            options={
                "verbose_name": "Local Faborito",
                "verbose_name_plural": "Locales Favoritos",
            },
        ),
    ]
