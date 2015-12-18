from django.conf.urls import include, url

from .views import ProductsView

urlpatterns = [
    url(r'^$', ProductsView.as_view(), name='products'),
]


