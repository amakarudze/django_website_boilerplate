from django.db import models
from django.utils import timezone


class Contact(models.Model):
    name = models.CharField("full name", max_length=120)
    phone = models.CharField("phone number", max_length=30, help_text = "Please include your country code.")
    email = models.EmailField("email address", max_length=120)
    subject = models.CharField(max_length=120)
    message = models.TextField()
    emaildate = models.DateTimeField(default=timezone.now)
    
    class Meta:
        managed = True

    def __str__(self):
        return self.name
