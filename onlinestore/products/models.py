from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.CASCADE, 
                                     related_name="products")
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    price = models.FloatField()

    def __str__(self):
        return self.name
