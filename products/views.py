from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import JsonResponse

def product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products.html', {'product': product})

def chains(request):
    products = Product.objects.filter(product_type='chain')
    return render(request, 'chains.html', {'products': products})

def rings(request):
    products = Product.objects.filter(product_type='ring')
    return render(request, 'rings.html', {'products': products})

def bracelets(request):
    products = Product.objects.filter(product_type='bracelet')
    return render(request, 'bracelets.html', {'products': products})

def pendants(request):
    products = Product.objects.filter(product_type='pendant')
    return render(request, 'pendants.html', {'products': products})

def earrings(request):
    products = Product.objects.filter(product_type='earring')
    return render(request, 'earrings.html', {'products': products})

def grills(request):
    products = Product.objects.filter(product_type='grill')
    return render(request, 'grills.html', {'products': products})

def tryout(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'tryout.html', {'product': product})

def get_product_ar_data(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return JsonResponse({
        'image_url': product.image.url,
        'product_type': product.product_type,
        'ar_settings':{
            'scale':1.0,
            'offset_x':0,
            'offset_y':0,
        }
    })
