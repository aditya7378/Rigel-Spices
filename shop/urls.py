from django.urls import path
from django.urls.conf import include

from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('productdetail/<int:prod_id>', views.productDetails, name='ProductDetails'),
    path('shop/cart/', include('cart.urls')),
]