from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone = models.CharField(max_length=20, blank=True)

#     def __str__(self):
#         return self.user.username

class Categories(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

class Products(models.Model):
    product_name = models.CharField(max_length=50)
    product_price = models.FloatField()
    product_description = models.TextField()
    product_image = models.ImageField(upload_to='products')
    product_category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(default=timezone.now)
    payment_amount = models.FloatField()
    status = models.CharField(max_length=50)
    # order_id = models.ForeignKey('Orders', on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)

class Orders(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=timezone.now)
    amount = models.FloatField()
    status = models.CharField(max_length=50)
    payment_id = models.ForeignKey(Payments, on_delete=models.CASCADE)

class OrderDetails(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()

    # def __str__(self):
    #     return self.product.product_name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()

    # def __str__(self):
    #     return self.product.product_name 