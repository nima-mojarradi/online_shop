from django.contrib import admin
from .models import Order, OrderDetail

admin.site.register(OrderDetail)
admin.site.register(Order)