from django.urls import path
from .views import (
    adminpage,
    customerpage
)

app_name = 'accounts'

urlpatterns = [
    path('', customerpage, name='customerpage'),
    path('admin/', adminpage, name='adminpage'),
]
