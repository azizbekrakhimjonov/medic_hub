from django.db import models

# Create your models here.
class Patient(models.Model):
    fullname = models.CharField(max_length=30)
    age = models.IntegerField(default=1)
    phone = models.IntegerField(default=0)
    address = models.TextField(default="")

