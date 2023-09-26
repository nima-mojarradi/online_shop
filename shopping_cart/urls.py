from django.urls import path
from . import views

urlpatterns = [
    # path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    # path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    # path('', views.cart, name='cart'),
    path('cart/', views.CartAPI.as_view(), name='cart_api'),
]

