from django.db import models


class Adjustment(models.Model):
    whatsapp = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
