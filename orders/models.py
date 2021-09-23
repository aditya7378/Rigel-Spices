from django.db import models
from shop.models import Product

# Create your models here.
class Order(models.Model):
    STATUS = (
        ('New' , 'New'),
        ('Accepted' , 'Accepted'),
        ('Completed' , 'Completed'),
        ('Rejected' , 'Rejected'),
    )
    

    order_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    phone_no = models.IntegerField(null=True)
    email = models.CharField(max_length=100)
    order_note = models.CharField(max_length=100, blank =True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=25, choices=STATUS, default='New')
    order_total = models.IntegerField()
    products = models.CharField(max_length=500, null=True)
    

    def __str__(self):
        return self.first_name

class OrderProduct(models.Model):
    # order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.product.name
    


