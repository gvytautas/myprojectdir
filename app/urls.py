from django.urls import path
from .views import products, product_create

urlpatterns = [
    path('', products, name='products'),
    path('create', product_create, name='product_create'),
]
