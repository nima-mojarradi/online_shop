from django.contrib import admin
from .models import CustomUser, Cart

admin.site.register(Cart)
admin.site.register(CustomUser)