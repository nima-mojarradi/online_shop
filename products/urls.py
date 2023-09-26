from django.urls import path
from .views import ShowAllProducts, ProductsSearch, PageNumberPagination

urlpatterns = [
    path('products/',ShowAllProducts.as_view(),name='products'),
    path('search/',ProductsSearch.as_view(),name='search_products'),
]