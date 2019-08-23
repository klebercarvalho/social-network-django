from django.db import models

# Create your models here.

class Profile(models.Model):

    name = models.CharField(max_length=255, name=False)
    email = models.CharField(max_length=255, name=False)
    phone = models.CharField(max_length=15, name=False)
    company = models.CharField(max_length=255, name=False)
