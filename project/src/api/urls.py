from django.conf.urls import include, url

from src.api.views import ListProductsView


urlpatterns = [
    url(r'^list-products/', ListProductsView().as_view(), name='list_products'),
]

