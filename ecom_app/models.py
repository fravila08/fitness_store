
from django.db import models
# Create your models here.
class Cart(models.Model):
    img_url=models.CharField(max_length=500)
    title=models.CharField(max_length=250)
    price=models.FloatField(default=0)
    
    def __str__(self):
        return f'{self.title}'


class Fitness(models.Model):
    img_url=models.CharField(max_length=500)
    title=models.CharField(max_length=250)
    price=models.FloatField(default=0)
    
    def __str__(self):
        return f'{self.title}'
    
class Barbells(models.Model):
    img_url=models.CharField(max_length=500)
    title=models.CharField(max_length=250)
    price=models.FloatField(default=0)
    
    def __str__(self):
        return f'{self.title}'
    
    
class Dumbbells(models.Model):
    img_url=models.CharField(max_length=500)
    title=models.CharField(max_length=250)
    price=models.FloatField(default=0)
    
    def __str__(self):
        return f'{self.title}'