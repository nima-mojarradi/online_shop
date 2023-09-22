from django.db import models
from accounts.models import CustomUser
from products.models import Products


class Order(models.Model):
    payment_status = [("U", "Unpaid"), ("P", "Paid")]
    status_choices = [('P', 'Processing'), ('A', 'Approved'), ('C', 'Canceled')]
    order_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    status = models.CharField(max_length=1, choices=status_choices, default="P")
    payment = models.CharField(max_length=1, choices=payment_status, default="U")



class OrderDetail(models.Model):
    order = models.ForeignKey(Order, null=True, on_delete=models.PROTECT)
    product = models.ManyToManyField(Products)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, editable=False)



        


    