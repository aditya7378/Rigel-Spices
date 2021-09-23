from django.db import models
from shop.models import Product
# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=150, blank=True, null=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Cart ID: "+ self.cart_id
    
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    cart    = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    
    def get_quantitywise_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return "Product: "+self.product.name