from django.contrib import admin
from .models import  Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'product_type', 'image')
    search_fields = ('name',)
    list_filter = ('product_type',)

