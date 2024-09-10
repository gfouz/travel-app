from django.db import models


class Adjustment(models.Model):
    role= models.CharField(max_length=255, default='Ajustes')
    whatsapp = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
