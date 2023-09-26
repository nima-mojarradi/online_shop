from django.shortcuts import render
from rest_framework.generics import ListAPIView,ListCreateAPIView
from rest_framework.views import APIView
from .serializers import ProductSerializer
from .models import Products
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination

class ShowAllProducts(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Products.objects.all()
        title = self.request.query_params.get('title')
        if title is not None:
            queryset = queryset.filter(title=title)
        return queryset
    

class ProductsSearch(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        title = self.request.query_params.get('title', '')
        brand = self.request.query_params.get('brand', '')
        category = self.request.query_params.get('category', '')
        queryset = self.queryset
        print(self.request.query_params)
        if title:
            queryset = queryset.filter(Q(title__icontains=title))
        if brand:
            queryset = queryset.filter(Q(brand__title__icontains=brand))
        if category:
            queryset = queryset.filter(Q(category__name__icontains=category))
        return queryset
    
class PaginationView(APIView, PageNumberPagination):
    serializer_class = ProductSerializer

    def get(self,request):
        entity = Products.objects.all()
        results = self.paginate_queryset(entity, request)
        serializer = ProductSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)