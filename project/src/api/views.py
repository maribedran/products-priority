# coding: utf-8
from rest_framework import generics, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView

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


class UpdateManyProductsView(APIView):
    queryset = Product.objects.all()

    def post(self, request, *args, **kwargs):
        try:
            data = dict(request.data)
            update_ids = data['update_ids']
            priority = data['priority']
        except KeyError:
            return Response({'errors': 'Bad configured data'}, status=status.HTTP_400_BAD_REQUEST)

        self.queryset.filter(id__in=update_ids).update(priority=priority)
        return Response('OK', status=status.HTTP_201_CREATED)
