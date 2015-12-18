# coding: utf-8
from rest_framework import generics
from rest_framework.exceptions import PermissionDenied

from src.api.models import Product
from src.api.serializers import ProductSerializer


class ListProductsView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UpdateProductView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id'
    allowed_update_fields = ['priority']

    def post(self, request, *args, **kwargs):
        if request.POST.keys() != self.allowed_update_fields:
            raise PermissionDenied
        return self.partial_update(request, *args, **kwargs)
