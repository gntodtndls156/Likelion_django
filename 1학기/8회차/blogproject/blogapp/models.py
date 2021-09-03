from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.TextField(max_length=500, blank=True)
    email = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)