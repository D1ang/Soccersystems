from django.urls import path
from .views import CheckoutView, PaymentView

app_name = 'checkout'

urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('payment/', PaymentView.as_view(), name='payment'),
]