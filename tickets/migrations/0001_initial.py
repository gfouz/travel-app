# Generated by Django 5.0.2 on 2024-08-25 16:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("flights", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Ticket",
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
                    "cover_photo",
                    models.ImageField(blank=True, null=True, upload_to="cover_photos/"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("draft", "Draft"),
                            ("available", "Available"),
                            ("unavailable", "Unavailable"),
                        ],
                        max_length=15,
                    ),
                ),
                ("airline", models.CharField(max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("description", models.TextField(blank=True)),
                ("last_reservation_date", models.DateTimeField()),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "flights",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="flights.flight"
                    ),
                ),
                (
                    "ticket_issuer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Flight",
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
                ("from_location", models.CharField(max_length=255)),
                ("to_location", models.CharField(max_length=255)),
                ("flight_number", models.CharField(max_length=255)),
                ("date", models.DateField()),
                ("departure_time", models.TimeField()),
                ("arrival_time", models.TimeField()),
                ("luggage", models.IntegerField()),
                (
                    "ticket",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tickets.ticket"
                    ),
                ),
            ],
        ),
    ]
