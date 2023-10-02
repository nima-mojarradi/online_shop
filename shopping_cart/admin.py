from django.contrib import admin
from .models import Order, OrderDetail, CartItem

admin.site.register(OrderDetail)
admin.site.register(Order)
admin.site.register(CartItem)
