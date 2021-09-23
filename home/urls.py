from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/', views.about, name='about'),
    path('displaywish/', views.displaywish, name='displaywish'),
    path('Wishlist/<int:product_id>/',views.wishlist, name="Wishlist"),
    path("remove_wish/<int:product_id>/", views.remove_wish, name="remove_wish"),
    path('blog/',views.blog, name="blog"),
    path('contact/',views.contact, name="contact"),
    path('pulses/', views.pulses, name='pulses'),
    path('oil/', views.pulses, name='oil'),
    path('ourstory/', views.ourstory, name='ourstory'),
]