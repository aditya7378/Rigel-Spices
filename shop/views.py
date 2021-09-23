from django.shortcuts import render
from django.shortcuts import render
from . models import Product, ProductImages
# Create your views here.
def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html',{"products":products})


def productDetails(request, prod_id):
    product = Product.objects.get(id=prod_id)
    product_images = ProductImages.objects.filter(product_id=prod_id)
    return render(request, 'Product_detail.html',{"product":product, "Images":product_images})