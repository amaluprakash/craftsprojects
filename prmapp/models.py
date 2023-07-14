from django.db import models

# Create your models here.
class product(models.Model):
    file=models.FileField(default='0')
    name = models.CharField(max_length=40)
    description= models.CharField(max_length=40)
    type= models.CharField(max_length=40)

class register(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField()
    password=models.CharField(max_length=40)
