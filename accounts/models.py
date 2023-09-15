from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class CustomUser(AbstractBaseUser):
    username = models.CharField('Username', max_length=100, unique=True),
    first_name = models.CharField('first_name', max_length=100)
    last_name = models.CharField('last_name', max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.BigIntegerField(null=True, blank=True)
    cart_info = models.ForeignKey('Cart',on_delete=models.CASCADE)

    def __str__(self):
        return self.username
    


class Cart(models.Model):
    user = models.OneToOneField("CustomUser", on_delete=models.CASCADE)
    cart_number = models.BigIntegerField('cart_no')    