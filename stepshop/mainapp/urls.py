
from django.urls import path

from .views import index, about, contacts, product, products

urlpatterns = [
    path('', index),
    path('about/', about),
    path('contacts/', contacts),
    path('product/', product),
    path('products/', products),
]
