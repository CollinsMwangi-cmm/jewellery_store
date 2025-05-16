from django.db import models

# Create your models here.
class home_image(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField( upload_to='dashboard/',)
    description = models.CharField (max_length=150)
    
    def __str__(self):
        return self.name