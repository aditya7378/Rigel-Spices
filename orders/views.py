from django.shortcuts import render, redirect
from cart.models import CartItem
from cart.views import _cart_id
from .forms import OrderForm
from .models import Order, OrderProduct
from cart.models import Cart
from django.http import HttpResponse
from orders.models import OrderProduct

# Create your views here.
def place_order(request, quantity=0,total = 0):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_items = CartItem.objects.filter(cart_id=cart)
    print(cart_items)
    cart_count = cart_items.count()
    if cart_count <=0:
        return redirect('shop')
    
    
    for cart_item in cart_items:
        total += (cart_item.product.price* cart_item.quantity)
        quantity += cart_item.quantity
    total=total+59
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.country = form.cleaned_data['country']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.state = form.cleaned_data['state']
            data.pincode = form.cleaned_data['pincode']
            data.phone_no = form.cleaned_data['phone_no']
            data.email = form.cleaned_data['email']
            data.order_note = form.cleaned_data['order_note']
            data.order_total = total
            data.save()


            for cart_item in cart_items:
                orderproduct = OrderProduct()
                # orderproduct.order_number = order.id
                orderproduct.product_id = cart_item.product_id
                orderproduct.quantity = cart_item.quantity
                orderproduct.ordered = True
                orderproduct.save()

            cart_items = CartItem.objects.filter(cart_id=cart).delete()



           
        else:
            print("Error")
    else:
        print("Post request not ")
    return redirect ('thankyou')

def thankyou(request):
    return render(request,'thankyou.html')

def myorders(request):
    order_items = OrderProduct.objects.all()
    return render(request,'my_orders.html', {'orders':order_items})






    




