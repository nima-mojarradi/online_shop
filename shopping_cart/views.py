from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from products.models import Products
from .models import Order, OrderDetail
from .serializers import OrderDetailSerializer, OrderSerializer
from rest_framework import generics, permissions, status
from products.serializers import ProductSerializer
from rest_framework.views import APIView

class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

def calculate_total_price(request, pk):
    order_detail = OrderDetail.objects.get(pk=pk)
    total_price = 0
    for product in order_detail.product.all():
        total_price += product.unit_price * order_detail.quantity
    order_detail.price = total_price
    order_detail.save()
    return Response({"total_price": total_price}, status=status.HTTP_200_OK)

def add_product_to_cart(request, pk):
    order = Order.objects.get(pk=pk)
    product = Products.objects.get(pk=request.data['product_id'])
    order_detail, created = OrderDetail.objects.get_or_create(order=order)
    order_detail.product.add(product)
    order_detail.quantity += 1
    order_detail.save()
    return Response({"message": "Product added to cart"}, status=status.HTTP_201_CREATED)

def remove_product_from_cart(request, pk):
    order_detail = OrderDetail.objects.get(pk=pk)
    product = Products.objects.get(pk=request.data['product_id'])
    order_detail.product.remove(product)
    order_detail.quantity -= 1
    order_detail.save()
    return Response({"message": "Product removed from cart"}, status=status.HTTP_200_OK)