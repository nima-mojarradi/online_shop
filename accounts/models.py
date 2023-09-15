from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return self.username
    


class Cart(models.Model):
    user = models.OneToOneField("CustomUser", on_delete=models.CASCADE, unique=True)
    cart_number = models.CharField(max_length=20,verbose_name='cart_no')