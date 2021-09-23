from django.urls import path, include
from . import views
urlpatterns = [
    path('place_order/', views.place_order, name='place_order'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('myorders/', views.myorders, name='myorders'),


]