from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views.generic import View
from orders.models import Order
from .models import Payment
from decimal import Decimal
import datetime
import random
import string


def generate_id_code():
    """
    Using random to create an order ID
    Random is based on 8 digits.
    """
    return ''.join(
        random.choices(string.ascii_uppercase + string.digits, k=8)
    )


class PaymentView(LoginRequiredMixin, View):
    """
    Load the payment view and loads the public
    Stripe key for the card field.
    """
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            tax = order.get_total() * Decimal(21 / 100)
            total = order.get_total() + tax

            if total < 0:
                messages.warning(self.request, 'Your cart is empty')
                return redirect('products:products')   # <----- needs to be fixed

            template = 'checkout/payment.html'
            context = {
                'order': order,
                'tax': tax,
                'total': total
            }
            return render(self.request, template, context)

        except ObjectDoesNotExist:
            messages.warning(self.request, 'There is no active order')
            return redirect('orders:cart')

    def post(self, *args, **kwargs):
        """
        When POST payment will be created in the database
        and on Stripe.
        """
        order = Order.objects.get(user=self.request.user, ordered=False)
        tax = order.get_total() * Decimal(21 / 100)
        total = order.get_total() + tax
        amount = int(total * 100)

        # Creating the payment
        payment = Payment()
        payment.user = self.request.user
        payment.amount = amount
        payment.save()

        # Assign payment to order
        order_items = order.items.all()
        order_items.update(ordered=True)
        for item in order_items:
            item.save()

        order.ordered = True
        order.payment = payment
        order.total = total
        order.tax = tax

        order.id_code = '920-' + generate_id_code()
        order.save()

        messages.success(self.request, 'Your order was successful!')
        return redirect('accounts:employee')
