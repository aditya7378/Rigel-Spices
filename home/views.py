from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product
from .models import Wishlist

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def displaywish(request):
    items = Wishlist.objects.all()
    return render(request, 'Wishlist.html', {'items': items})

def wishlist(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        wish_items = Wishlist.objects.get(product=product)
        wish_items.save()
        
    except Wishlist.DoesNotExist:
        wish_items = Wishlist.objects.create(
             product=product,
        )
        wish_items.save()
        
    items = Wishlist.objects.all()

    return render(request, 'Wishlist.html', {'items': items})

def remove_wish(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wish_items = Wishlist.objects.get(product=product)
    wish_items.delete()
    return redirect('displaywish')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def pulses(request):
    return render(request,'pulses.html')


def oil(request):
    return render(request,'oil.html')


def ourstory(request):
    return render(request,'ourstory.html')