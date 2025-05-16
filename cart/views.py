from django.shortcuts import render, get_object_or_404
from products.models import Product
from django.http import JsonResponse
from .cart import Cart

def cart(request):
    cart_obj = Cart(request)
    cart_products = cart_obj.get_prods()
    quantities = cart_obj.get_quants()
    return render(request, 'cart.html', {'cart_products': cart_products, 'quantities': quantities, })

def add_to_cart(request):
    cart = Cart(request)
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product_qty = int(request.POST.get('product_qty', 1))

        if product_id:
            try:
                product = get_object_or_404(Product, id=product_id)
                cart.add(product=product, quantity=product_qty)
                cart_quantity = cart.__len__()
                return JsonResponse({'qty': cart_quantity})
            except Exception as e:
                return JsonResponse({'success': False, 'message': str(e)}, status=500)
        else:
            return JsonResponse({'success': False, 'message': 'Product ID not provided.'}, status=400)

def delete_cart(request):
    # Implement logic here to delete an item from the cart
    pass

def update_cart(request):
    # Implement logic here to update a cart item quantity
    pass
