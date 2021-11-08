import os
import requests
from requests.exceptions import HTTPError
from datetime import date

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import request
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from django.views.generic import View
from orders.models import Order
from .forms import CheckoutForm
from django.template.loader import get_template
from django.core.mail import EmailMessage


class CheckoutView(LoginRequiredMixin, View):
    """
    Load the checkout view for the order
    including the form. On POST save the
    order to the backend & Adfas.
    """
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            tax = order.get_total() / 100 * 21
            total = order.get_total() + tax

            if total <= 0:
                message = _('Your cart is empty')
                messages.warning(self.request, message=message)

                return redirect('products:products')
            else:
                form = CheckoutForm()
                context = {
                    'order': order,
                    'tax': tax,
                    'total': total,
                    'form': form
                }
                return render(self.request, 'checkout/details.html', context)

        except ObjectDoesNotExist:
            message = _('There is no active order')
            messages.warning(self.request, message=message)
            return redirect('products:products')

    def post(self, *args, **kwargs):
        """
        POST, order will be created in the database
        & processed to Adfas trough the Adfas-WS API.
        """
        form = CheckoutForm(self.request.POST, self.request.FILES or None)

        try:
            order = Order.objects.get(user=self.request.user, ordered=False)

            if form.is_valid():

                # Grab form fields & order data for serialisation.
                comments = form.cleaned_data.get('comments')
                delivery_date = form.cleaned_data.get('delivery_date')

                def order_serializer(self):
                    order = Order.objects.get(user=self.request.user, ordered=False)
                    order_items = list(order.items.all().values('article_id', 'description', 'quantity'))

                    for item in order_items:
                        item["artnr"] = item.pop("article_id")
                        item["omsch"] = item.pop("description")
                        item["aantl"] = item.pop("quantity")
                        item["lvdat"] = str(delivery_date)

                    data = {
                        "workorder": {
                            "nawnr": "016311",
                            "datum": str(date.today()),
                            "lvdat": str(delivery_date),
                            "uwref": str(order.shop),
                            "exref": comments,
                            "dirjn": "false",         # Direct delivery
                            "bvwnr": "0001",          # Terms of payment
                            "kstvv": 0,               # Transport costs
                            "orderlines": order_items
                        }
                    }
                    return data

                try:
                    # Adfas-WS connection
                    url = os.environ.get('ADFAS_WS')
                    set_order = requests.post(url, json=order_serializer(self))
                    set_order.raise_for_status()
                    response = set_order.json()

                except HTTPError as http_err:
                    print(f'HTTP error occurred: {http_err}')

                except Exception as err:
                    print(f'Other error occurred: {err}')

                # Set all order items to be ordered.
                order_items = order.items.all()
                order_items.update(ordered=True)
                for item in order_items:
                    item.save()

                order.comments = comments
                order.delivery_date = delivery_date
                order.ordered = True
                order.id_code = response['ordnr']

                # Create the email on the contact template & send.
                template = get_template('placed_order.html')
                context = {
                    'reference': order_serializer(self)["workorder"]["uwref"],
                    'comments': comments,
                    'delivery_date': delivery_date,
                }
                content = template.render(context)

                email = EmailMessage(
                    "Soccersystems order",
                    content,
                    "info@ibsgraphics.nl" + '', ['info@ibsgraphics.nl'],
                    headers={'Reply-To': 'info@ibsgraphics.nl'}
                )

                email.send()
                order.save()

                message = _('Your order was successful!')
                messages.success(self.request, message=message)

                return redirect('accounts:employee')

        except ObjectDoesNotExist:
            message = _('There is no active order')
            messages.warning(self.request, message=message)

            return redirect('checkout:checkout')
