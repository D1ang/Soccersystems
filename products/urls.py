from django.urls import path
from .views import product_items_list

app_name = 'products'

urlpatterns = [
    path('products/', product_items_list, name='products'),
]
