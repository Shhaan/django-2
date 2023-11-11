from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class game(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='image')
    des = models.CharField(max_length=200)
    url = models.CharField(max_length=20)
    def __str__(self) :
        return self.title
class feeds(models.Model):
    feedback = models.TextField(max_length=2000,null=False)  
    ratings = models.CharField(max_length=2)  
