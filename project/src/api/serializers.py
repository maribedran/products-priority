# coding: utf-8
from rest_framework import serializers

from src.api.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'priority')

