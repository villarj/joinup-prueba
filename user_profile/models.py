from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(max_length=50, unique=True)
    mobile_phone = models.CharField(max_length=20, unique=True)
    hobbies = models.TextField(max_length=200)