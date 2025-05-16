from django.db import models

# Create your models here.

class Product(models.Model):
    PRODUCT_TYPES = [
        ('chain', 'Chain'),
        ('bracelet', 'Bracelet'),
        ('earring', 'Earring'),
        ('grill', 'Grill'),
        ('pendant', 'Pendant'),
        ('ring', 'Ring'),
    ]
    
    name = models.CharField (max_length=50)
    price = models.DecimalField(default='0', max_digits=10, decimal_places=2)
    image = models.ImageField (upload_to='products/')
    description = models.CharField(max_length=150, default='', blank=True, null=True)
    product_type = models.CharField(max_length=20, choices =PRODUCT_TYPES, default='chain')
    sale_price = models.DecimalField(default='0', max_digits=10, decimal_places=2)
    is_sale = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.name
    
