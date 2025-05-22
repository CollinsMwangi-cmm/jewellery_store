from products.models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart
        
    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = int(quantity)
        
        if product_qty > 0:
            self.cart[product_id] = product_qty
        else:
            self.cart.pop(product_id, None)  
            
        self.session.modified = True
    
    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products
    
    def get_quants(self):
        return self.cart


    def remove (self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
            return True
        return False

    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True

    def get_total(self):
        try:
            product_ids = self.cart.keys()
            products = Product.objects.filter(id__in=[int(id) for id in product_ids])
            total = 0
            for product in products:
                total += float(product.price) * int(self.cart[str(product.id)])
            return total
        except Exception as e:
            logger.error(f"Error calculating cart total: {str(e)}")
            return 0

    def clear(self):
        self.cart = {}
        self.save()