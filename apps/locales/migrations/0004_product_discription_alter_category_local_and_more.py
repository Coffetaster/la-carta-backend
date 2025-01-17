# Generated by Django 5.0.2 on 2024-02-28 08:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("locales", "0003_gallery_image_local_image_product_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="discription",
            field=models.TextField(
                default="Descripcion del producto",
                max_length=255,
                verbose_name="Detalles",
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="local",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="locales.local",
                verbose_name="categoryLocal",
            ),
        ),
        migrations.AlterField(
            model_name="gallery",
            name="local",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="locales.local",
                verbose_name="galleryLocal",
            ),
        ),
    ]
