from django.contrib import admin
from .models import Category, Product, ProductImages
import admin_thumbnails
# Register your models here.

@admin_thumbnails.thumbnail('product_img')
class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','category','price','in_stock')
    inlines = [ProductImagesInline]


admin.site.register(Category),
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImages),