from django.urls import path
from .views import employee, supervisor, orderdetails

app_name = 'accounts'

urlpatterns = [
    path('', employee, name='employee'),
    path('supervisor/', supervisor, name='supervisor'),

    path('orderdetails/<str:pk_order>/', orderdetails, name='orderdetails'),
]
