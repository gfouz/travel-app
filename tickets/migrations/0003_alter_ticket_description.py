# Generated by Django 5.0.2 on 2024-09-05 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tickets", "0002_alter_ticket_flights_alter_ticket_ticket_issuer_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticket",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
