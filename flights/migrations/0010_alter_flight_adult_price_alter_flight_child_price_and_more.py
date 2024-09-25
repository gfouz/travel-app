# Generated by Django 5.0.2 on 2024-09-24 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flights", "0009_alter_flight_adult_price_alter_flight_child_price_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flight",
            name="adult_price",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name="flight",
            name="child_price",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name="flight",
            name="infant_price",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
