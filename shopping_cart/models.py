from django.db import models
from accounts.models import CustomUser
from products.models import Products
from accounts.models import Cart


class Order(models.Model):
    payment_status = [("U", "Unpaid"), ("P", "Paid")]
    status_choices = [('P', 'Processing'), ('A', 'Approved'), ('C', 'Canceled')]
    order_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    status = models.CharField(max_length=1, choices=status_choices, default="P")
    payment = models.CharField(max_length=1, choices=payment_status, default="U")

    @property
    def get_order_items(self):
        order_items = OrderDetail.objects.filter(order=self.id)
        return order_items

    @property
    def total_price(self):
        order_detail = self.get_order_items
        order_total_price = 0
        for item in order_detail:
            order_total_price += item.total_price
        return order_total_price


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, null=True, on_delete=models.PROTECT)
    product = models.ManyToManyField(Products)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, editable=False)

    @property
    def total_price(self):
        if self.price and self.quantity:
            return self.price * self.quantity
        else:
            return 0

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    @property
    def total_quantity(self):
        for item in CartItem.item:
            if item in CartItem.item:
                self.quantity += 1

                