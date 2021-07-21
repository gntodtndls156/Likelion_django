from django.db import models

# Create your models here.
class Member(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    major = models.CharField(max_length=100)
    year = models.IntegerField(blank=True, null=True)
    old = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name