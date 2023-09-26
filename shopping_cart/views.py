from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from products.models import Products
from products.serializers import ProductSerializer
from rest_framework.views import APIView


class CartAPI(APIView):
    @csrf_exempt
    def get(self, request):
        if 'cart' not in request.session:
            request.session['cart'] = []
        products = Products.objects.filter(id__in=request.session['cart'])
        serializer = ProductSerializer(products, many=True)
        total_price = sum([product.unit_price for product in products])
        return Response({'products': serializer.data, 'total_price': total_price})