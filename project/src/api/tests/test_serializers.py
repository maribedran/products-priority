# coding: utf-8
from django.test import TestCase
from model_mommy import mommy

from src.api.models import Product
from src.api.serializers import ProductSerializer

class ProductSerializerTest(TestCase):

    def setUp(self):
        self.serializer = ProductSerializer
        self.product = mommy.make(Product)

    def test_serializer_returns_correct_data(self):
        data = self.serializer(self.product).data
        expected_data = {
            'id': self.product.id,
            'name': self.product.name,
            'priority': self.product.priority,
        }
        self.assertEqual(expected_data, data)
