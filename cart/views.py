from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart
from django.http import JsonResponse
from .cart import Cart
from django.core.exceptions import ValidationError
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
import logging
import  json
from django.views.decorators.http import require_POST

logger = logging.getLogger(__name__)

def cart(request):
    cart_obj = Cart(request)
    cart_products = cart_obj.get_prods()
    quantities = cart_obj.get_quants()
    return render(request, 'cart.html', {'cart_products': cart_products, 'quantities': quantities})

@csrf_protect
@require_http_methods(["POST"])
def add_to_cart(request):
    cart = Cart(request)
    
    product_id = request.POST.get('product_id')
    if not product_id:
        return JsonResponse({
            'success': False, 
            'message': 'Product ID not provided.'
        }, status=400)
    
    try:
        product_qty = int(request.POST.get('product_qty', 1))
        if product_qty <= 0:
            raise ValidationError('Quantity must be positive')
        if product_qty > 100:  # Example maximum limit
            raise ValidationError('Quantity exceeds maximum limit')
            
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)
        cart_quantity = cart.__len__()
        
        return JsonResponse({
            'success': True,
            'qty': cart_quantity
        })
        
    except ValueError:
        return JsonResponse({
            'success': False,
            'message': 'Invalid quantity provided'
        }, status=400)
    except ValidationError as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        }, status=400)
    except Exception as e:
        logger.error(f"Error adding product {product_id} to cart: {str(e)}")
        return JsonResponse({
            'success': False,
            'message': 'An error occurred while adding to cart'
        }, status=500)


@csrf_protect
@require_POST
def delete_cart(request, product_id):
    try:
        cart = Cart(request)
        if cart.remove(product_id):
            cart_total = cart.get_total()
            cart_qty = len(cart)

            return JsonResponse({
                'status': 'success',
                'qty': cart_qty,
                'total_price': "{:.2f}".format(cart_total)
            })
        else:
            return JsonResponse({
                'error': 'Product not found in cart'
            }, status=404)

    except Exception as e:
        logger.error(f"Error removing product {product_id} from cart: {str(e)}")
        return JsonResponse({
            'error': str(e)
        }, status=400)

def update_cart(request):
    # Implement logic here to update a cart item quantity
    pass