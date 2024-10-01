# Generated by Django 5.0.2 on 2024-09-29 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tickets", "0007_alter_ticket_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ticket",
            name="description",
        ),
        migrations.RemoveField(
            model_name="ticket",
            name="last_reservation_date",
        ),
        migrations.AlterField(
            model_name="ticket",
            name="airline",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="last_name",
            field=models.CharField(blank=True, default="", max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="status",
            field=models.CharField(
                choices=[("reserved", "Reserved"), ("expired", "Expired")],
                default="scheduled",
                max_length=15,
            ),
        ),
    ]
