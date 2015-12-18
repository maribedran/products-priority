from django.conf.urls import url

from src.api.views import ListProductsView, UpdateProductView, UpdateManyProductsView


urlpatterns = [
    url(r'^list-products/', ListProductsView().as_view(), name='list_products'),
    url(r'^update-product/(?P<product_id>\d+)/', UpdateProductView().as_view(), name='update_product'),
    url(r'^update-many/', UpdateManyProductsView().as_view(), name='update_many'),
]
