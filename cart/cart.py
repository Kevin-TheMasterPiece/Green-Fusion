from decimal import Decimal
from django.conf import settings
from administrador.models import ensaladas


class Cart:
    def __init__(self, request):
       
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
    
    def add(self, ensalada, precio_base, tamaño, quantity=1, override_quantity=False):
        
        product_id = str(ensalada.ID_ensalada)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(precio_base),
                                     'tamaño': str(tamaño)}
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        
        self.session.modified = True
    
    def remove(self, ensalada):
       
        product_id = str(ensalada.ID_ensalada)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    
    def __iter__(self):
        
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        ensaladas_carrito = ensaladas.objects.filter(ID_ensalada__in=product_ids)
        cart = self.cart.copy()
        for ensalada in ensaladas_carrito:
            cart[str(ensalada.ID_ensalada)]['product'] = ensalada
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
    
        return sum(item['quantity'] for item in self.cart.values())
    
    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())