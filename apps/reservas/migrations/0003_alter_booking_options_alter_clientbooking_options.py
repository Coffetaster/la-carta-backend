# Generated by Django 5.0.2 on 2024-03-04 14:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("reservas", "0002_booking_active"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="booking",
            options={"verbose_name": "Local", "verbose_name_plural": "Locales"},
        ),
        migrations.AlterModelOptions(
            name="clientbooking",
            options={
                "verbose_name": "Reservación de cliente",
                "verbose_name_plural": "Reservaciones de clientes",
            },
        ),
    ]
