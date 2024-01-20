from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class APIUser(AbstractUser):
    pass

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    description = models.TextField(max_length=500, null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    image = models.FileField(upload_to='products')

class Basket(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(APIUser, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

class BasketItem(models.Model):
    id = models.AutoField(primary_key=True)
    basket_id = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def product_name(self):
        return self.product_id.name

    def price(self):
        return self.product_id.price * self.quantity
    
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    datetime_ordered = models.DateTimeField(auto_now_add=True)
    basket_id = models.ForeignKey(Basket, on_delete=models.CASCADE)
    user_id = models.ForeignKey(APIUser, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    shipping_address = models.TextField(default="")