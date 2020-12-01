from django.urls import path
from .views import PaymentView

app_name = 'checkout'

urlpatterns = [
    path('payment/', PaymentView.as_view(), name='payment'),
]
