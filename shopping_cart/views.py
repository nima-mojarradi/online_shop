from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from products.models import Products
from .models import Order, OrderDetail, CartItem
from .serializers import OrderDetailSerializer, OrderSerializer
from rest_framework import generics, permissions, status
from products.serializers import ProductSerializer
from rest_framework.views import APIView
from accounts.models import Cart
from .serializer import CartItemSerializer


class CartView(APIView):
    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            cart_item = CartItem.objects.get(pk=pk)
            cart_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CartItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

