from django.contrib import admin
from .models import home_image

class HomeImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  
    search_fields = ('name', 'description') 


admin.site.register(home_image, HomeImageAdmin)
