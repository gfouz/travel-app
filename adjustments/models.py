from django.db import models 

class Setting(models.Model):
    whatsapp = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    available_days = models.IntegerField(blank=True, null=True)
    unavailable_days = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if Setting.objects.exists() and not self.pk:
            raise ValueError("Only one Setting instance can exist.")
        super().save(*args, **kwargs)    


