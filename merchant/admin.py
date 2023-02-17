from django.contrib import admin
from .models import Categories, Products, Payments, Orders, OrderDetails

# Register your models here.
admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(Payments)
admin.site.register(Orders)
admin.site.register(OrderDetails)
