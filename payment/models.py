from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50, null=True, blank=True)
    zipcode = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        validators=[RegexValidator(r'^\d{5}(-\d{4})?$', 'Enter a valid zip code.')]
    )
    country = models.CharField(max_length=100)  # Changed from county
    
    class Meta:
        verbose_name_plural = "Shipping Addresses"

    def __str__(self):
        return f'ShippingAddress - {self.full_name} ({self.id})'