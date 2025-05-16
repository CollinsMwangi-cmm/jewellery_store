from django.shortcuts import render
from .models import home_image

# Create your views here.

def home (request):
    return render(request, ('home.html'))

def home_details (request):
    images = home_image.objects.all()
    return render(request, 'home_details.html', {'images': images} )

