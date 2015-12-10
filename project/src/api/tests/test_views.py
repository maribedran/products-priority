# coding: utf-8
import json
from django.test import TestCase
from model_mommy import mommy

from django.core.urlresolvers import reverse

from src.api.models import Product
from src.api.views import ListProductsView


class ListProductsViewTest(TestCase):

    def setUp(self):
        self.url = reverse('api:list_products')
        self.product1 = mommy.make(Product)
        self.product2 = mommy.make(Product)

    def test_response_returns_status_code_200(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)

    def test_response_has_coorect_data(self):
        response = self.client.get(self.url)
        expected_data = [
            {
                'id': self.product1.id,
                'name': self.product1.name,
                'priority': self.product1.priority,
            },
            {
                'id': self.product2.id,
                'name': self.product2.name,
                'priority': self.product2.priority,
            },
        ]
        self.assertEqual(expected_data, json.loads(response.content))
