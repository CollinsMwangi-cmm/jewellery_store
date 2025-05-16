from products.models import Product

class Cart():
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
