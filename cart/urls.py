from django.urls import path, include
from . import views
urlpatterns = [
    path("cart/", views.cart, name="cart"),
    path("add_cart/<int:product_id>/", views.add_cart, name="add_cart"),
    path("minus_cart/<int:product_id>/", views.minus, name="minus_cart"),
    path("remove_cart/<int:product_id>/", views.remove_cart, name="remove_cart"),
    path("checkout/",views.checkout, name='checkout'),
]