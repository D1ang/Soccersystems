from django.urls import path
from .views import (
    adminpage,
    customerpage,
    orderdetails
)

app_name = 'accounts'

urlpatterns = [
    path('', customerpage, name='customerpage'),
    path('admin/', adminpage, name='adminpage'),

    path('orderdetails/<str:pk_order>/', orderdetails, name='orderdetails'),
]
