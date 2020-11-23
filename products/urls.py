from django.urls import path
from .views import products_list, product_items

app_name = 'products'

urlpatterns = [
    path('products/', products_list, name='products'),

    path('product_items/<str:pk_product>/', product_items, name='product_items')
]
