from django.urls import path
from .views import employee, supervisor, orderdetails, invite

app_name = 'accounts'

urlpatterns = [
    path('', employee, name='employee'),
    path('supervisor/', supervisor, name='supervisor'),
    path('invite/', invite, name='invite'),

    path('orderdetails/<str:pk_order>/', orderdetails, name='orderdetails'),
]
