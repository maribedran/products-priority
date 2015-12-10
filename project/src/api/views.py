# coding: utf-8
from rest_framework import generics

from src.api.models import Product
from src.api.serializers import ProductSerializer


class ListProductsView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
