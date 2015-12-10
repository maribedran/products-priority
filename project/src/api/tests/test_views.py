# coding: utf-8
from django.test import TestCase
from model_mommy import mommy

from django.core.urlresolvers import reverse

from src.api.models import Product
from src.api.views import ListProductsView


class ListProductsViewTest(TestCase):

    def setUp(self):
        self.url = reverse('api:list_products')

    def test_response_returns_status_code_200(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
