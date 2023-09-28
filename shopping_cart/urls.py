from django.urls import path
from . import views

urlpatterns = [
    path('add_to_cart/', views.add_product_to_cart, name='cart_api'),
    path('remove_from_cart/', views.remove_product_from_cart),
    path('total_price/<int:pk>', views.calculate_total_price)
]

