from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=140, primary_key=True)
    password = models.CharField(max_length=140)
    