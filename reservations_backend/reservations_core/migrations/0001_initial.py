# Generated by Django 5.1.1 on 2024-11-10 01:50

import django.db.models.deletion
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Address",
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
                    "street",
                    models.CharField(max_length=100, verbose_name="street and number"),
                ),
                ("city", models.CharField(max_length=100, verbose_name="city")),
                ("country", models.CharField(max_length=100, verbose_name="country")),
                ("zip_code", models.CharField(max_length=10, verbose_name="zip code")),
            ],
        ),
        migrations.CreateModel(
            name="Facility",
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
                ("name", models.CharField(max_length=100, verbose_name="name")),
                ("description", models.TextField(verbose_name="description")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="facilities",
                        verbose_name="image",
                    ),
                ),
                ("price", models.FloatField(verbose_name="price per day")),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
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
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region="CZ", verbose_name="phone number"
                    ),
                ),
                (
                    "social_number",
                    models.CharField(max_length=20, verbose_name="social number"),
                ),
                (
                    "address",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="customers",
                        to="reservations_core.address",
                        verbose_name="address",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="customer",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Reservation",
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
                ("phone", models.CharField(max_length=20, verbose_name="phone number")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="created at"),
                ),
                ("datetime_from", models.DateTimeField(verbose_name="datetime from")),
                ("datetime_to", models.DateTimeField(verbose_name="datetime to")),
                ("party_size", models.IntegerField(verbose_name="party size")),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reservations",
                        to="reservations_core.customer",
                        verbose_name="customer",
                    ),
                ),
                (
                    "facility",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reservations",
                        to="reservations_core.facility",
                        verbose_name="facility",
                    ),
                ),
            ],
        ),
    ]