# coding: utf-8
from django.views.generic import TemplateView


class ProductsView(TemplateView):
    template_name = 'web_app/products.html'
