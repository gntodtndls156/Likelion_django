from django.db import models
from django.db.models.fields.files import ImageField
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=99, null=True, default='')
    age = models.IntegerField(default=2, null=True)
    pub_date = models.DateTimeField(default=timezone.now, null=True)
    email = models.EmailField(max_length=253, null=True, default='')
    introduce = models.TextField(null=True)
    image = ImageField(null=True)
    
    def __str__(self):
        return self.name