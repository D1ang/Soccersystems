from django.urls import path
from .views import ItemListView

app_name = 'products'

urlpatterns = [
    path('products/', ItemListView.as_view(), name='products'),
]
