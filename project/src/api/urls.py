from django.conf.urls import include, url

from src.api.views import ListProductsView, UpdateProductView


urlpatterns = [
    url(r'^list-products/', ListProductsView().as_view(), name='list_products'),
    url(r'^update-product/(?P<product_id>\d+)/', UpdateProductView().as_view(), name='update_product'),
]

