# Generated by Django 5.0.2 on 2024-08-22 20:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Adjustment",
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
                ("whatsapp", models.CharField(max_length=20)),
                ("email", models.EmailField(blank=True, max_length=254)),
            ],
        ),
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
                ("name", models.CharField(max_length=255)),
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
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
                        on_delete=django.db.models.deletion.CASCADE, to="travels.ticket"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CheckIn",
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
                ("fullname", models.CharField(max_length=255)),
                ("passport", models.CharField(max_length=50)),
                ("ticket_number", models.CharField(max_length=50)),
                ("reservation_code", models.CharField(max_length=50)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("draft", "Draft"),
                            ("pending", "Pending"),
                            ("completed", "Completed"),
                        ],
                        max_length=10,
                    ),
                ),
                ("created_by", models.CharField(max_length=255)),
                (
                    "attached_document",
                    models.FileField(blank=True, null=True, upload_to="documents/"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "ticket",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="travels.ticket"
                    ),
                ),
            ],
        ),
    ]
