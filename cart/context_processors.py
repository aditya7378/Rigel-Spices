from .models import Cart , CartItem
from .views import _cart_id
from home.models import Wishlist


def counter(request):
    cart_count = 0
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.all()
        for cart_item in cart_items:
            cart_count +=1
    
    except Cart.DoesNotExist:
        cart_count = 0


    return dict(cart_count=cart_count)

def wishcounter(request):
    wish_count = 0

    try:
        items = Wishlist.objects.all()
        for item in items:
            wish_count +=1
    
    except Wishlist.DoesNotExist:
        wish_count = 0

    return dict(wish_count=wish_count)