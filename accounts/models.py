from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.BigIntegerField(null=True, blank=True)
    address = models.ManyToManyField('Address')
    image = models.ImageField(upload_to='images/accounts',null=True)

    def __str__(self):
        return self.username
    
class Address(models.Model):
    location = models.CharField(max_length=255)

class Cart(models.Model):
    user = models.OneToOneField("CustomUser", on_delete=models.CASCADE, unique=True)
    cart_number = models.CharField(max_length=20,verbose_name='cart_no')