from django.db import models

# Create your models here.
from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category    = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name        = models.CharField(max_length=100, null=True)
    price       = models.FloatField(null=True)
    in_stock    = models.BooleanField(null=True)
    img         = models.ImageField(upload_to = 'PrimaryImages', null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.category.name+ " : " +self.name 

class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, null = True)
    product_img = models.ImageField(upload_to='images/product_images')

    class Meta:
        verbose_name_plural = 'Product Images'

    def __str__(self):
        return self.product.name
