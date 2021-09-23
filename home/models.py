from django.db import models
from shop.models import Product


# Create your models here.
class Wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.product.name
