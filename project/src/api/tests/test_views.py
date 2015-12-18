# coding: utf-8
import json
from django.test import TestCase
from model_mommy import mommy

from django.core.urlresolvers import reverse

from src.api.models import Product


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


class UpdateProductViewTest(TestCase):

    def setUp(self):
        self.url = reverse('api:update_product', args=[42])
        self.product = mommy.make(Product, id=42, priority=False, name='Name')

    def test_get_shows_products_info_correctly(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
        response_content = json.loads(response.content)
        self.assertEqual('Name', response_content['name'])
        self.assertEqual(42, response_content['id'])
        self.assertFalse(response_content['priority'])

    def test_post_updates_product_correctly(self):
        response = self.client.post(self.url, {'priority': True})

        self.assertEqual(200, response.status_code)
        self.assertTrue(Product.objects.get().priority)

    def test_view_allows_only_updating_priority_field(self):
        response = self.client.post(self.url, {'name': 'Name'})
        self.assertEqual(403, response.status_code)


class UpdateManyProductsViewTest(TestCase):

    def setUp(self):
        self.url = reverse('api:update_many')
        mommy.make(Product, id=1, priority=False)
        mommy.make(Product, id=2, priority=False)
        mommy.make(Product, id=3, priority=False)
        mommy.make(Product, id=4, priority=True)
        mommy.make(Product, id=5, priority=True)

    def test_post_updates_products_correctly(self):
        data = {
            'update_ids': [1, 2],
            'priority': True,
        }
        response = self.client.post(self.url, data)
        self.assertEqual(201, response.status_code)
        self.assertEqual(4, Product.objects.filter(priority=True).count())
        self.assertEqual(1, Product.objects.filter(priority=False).count())

    def test_corrupt_data_returns_400(self):
        response = self.client.post(self.url, {'update_ids': [10]})
        self.assertEqual(400, response.status_code)
