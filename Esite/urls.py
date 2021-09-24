from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('shop/', include('shop.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
<<<<<<< HEAD

=======
    admin.site.site_header  =  "Rigel Spices"  
    admin.site.site_title  =  "Rigel Spices"
    admin.site.index_title  =  "Rigel Spices"
>>>>>>> 099cd5879bf54f94694c82cbbf1ab11cf0c3e8ef
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
