from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.views.generic import View
from orders.models import Order
from .forms import CheckoutForm

from fmrest import dataAPI
from decimal import Decimal
import uuid

fm = dataAPI.DataAPIv1('fm.ibs-mijdrecht.nl')


class PaymentView(LoginRequiredMixin, View):
    """
    Load the checkout view for the order
    including the form. On POST save the
    order to the Postgres backend and FileMaker.
    """
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            tax = order.get_total() * Decimal(21 / 100)
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
                return render(self.request, 'checkout/payment.html', context)

        except ObjectDoesNotExist:
            message = _('There is no active order')
            messages.warning(self.request, message=message)
            return redirect('products:products')

    def post(self, *args, **kwargs):
        """
        On POST, payment will be created in the database
        and processed to the FileMaker data API.
        """
        form = CheckoutForm(self.request.POST, self.request.FILES or None)
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            tax = order.get_total() * Decimal(21 / 100)
            total = order.get_total() + tax

            if form.is_valid():
                # FileMaker data API - create a token to authenticate database
                fm.authenticate('Digitrans', 'cwp', 'cwp123')
                if fm.errorCode != 0:
                    print(fm.errorMessage)

                def fm_serializer(self):
                    shop = str(self.request.user.employee.shop)
                    order = Order.objects.get(user=self.request.user, ordered=False)
                    order_items = list(order.items.all().values('article_id', 'quantity'))

                    order.id_code = uuid.uuid1().int

                    for item in order_items:
                        item["Opdrachten::kf_web_order_id"] = order.id_code
                        item["Opdrachten::kf_artikelen_id"] = item.pop("article_id")
                        item["Opdrachten::order_soort"] = "Order"
                        item["Opdrachten::omschrijving"] = " "
                        item["Opdrachten::aantal_gereserveerd"] = item.pop("quantity")
                        item["Opdrachten::werkbon_status"] = 1

                    data = {
                        "fieldData": {
                            "kp_orderbeheer_id": order.id_code,
                            "kf_relatiebeheer_id": 92887518,
                            "order_soort": "Order",
                            "order_status": "Bevestigd",
                            "omschrijving": shop + " order",
                            "referentie": shop,
                        },
                        "portalData": {
                            "portal": order_items
                        }
                    }
                    return data

                fm.create_record('web_find_asset_detail', fm_serializer(self))
                fm.logout()

                # Save order to the backend
                comments = form.cleaned_data.get('comments')
                delivery_date = form.cleaned_data.get('delivery_date')

                order_items = order.items.all()
                order_items.update(ordered=True)
                for item in order_items:
                    item.save()

                order.comments = comments
                order.delivery_date = delivery_date
                order.ordered = True
                order.total = total
                order.tax = tax
                # order.id_code = '921-' + generate_id_code()

                order.save()

                message = _('Your order was successful!')
                messages.success(self.request, message=message)

                return redirect('accounts:employee')

        except ObjectDoesNotExist:
            message = _('There is no active order')
            messages.warning(self.request, message=message)

            return redirect('checkout:payment')
