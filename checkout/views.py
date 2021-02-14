from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views.generic import View
from orders.models import Order, OrderItem
from accounts.models import Employee
from .models import Payment

from fmrest import dataAPI
from decimal import Decimal
import uuid

fm = dataAPI.DataAPIv1('fm.ibs-mijdrecht.nl')


class PaymentView(LoginRequiredMixin, View):
    """
    Load the payment view for
    the order checkout.
    """
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            tax = order.get_total() * Decimal(21 / 100)
            total = order.get_total() + tax

            if total <= 0:
                messages.warning(self.request, 'Your cart is empty')
                return redirect('products:products')

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
        On POST, payment will be created in the database
        and on processed to the FileMaker data API.
        """
        # FileMaker data API - create a token to authenticate database
        fm.authenticate('Digitrans', 'cwp', 'cwp123')
        if fm.errorCode != 0:
            print(fm.errorMessage)

        def fm_serializer(self):
            shop = str(self.request.user.employee.shop)
            order = Order.objects.get(user=self.request.user, ordered=False)
            order_items = list(order.items.all().values('item', 'quantity'))

            order.id_code = uuid.uuid1().int

            for item in order_items:
                item["Opdrachten::kf_web_order_id"] = order.id_code
                item["Opdrachten::productgroep"] = "Transfers"
                item["Opdrachten::artikelnummer"] = item.pop("item")
                item["Opdrachten::aantal_gereserveerd"] = item.pop("quantity")

            data = {
                "fieldData": {
                    "kp_orderbeheer_id": order.id_code,
                    "order_soort": "Order",
                    "order_status": "Bevestigd",
                    "omschrijving": "Ajax order",
                    "referentie": shop,
                    "kf_relatiebeheer_id": 92887518,
                },
                "portalData": {
                    "portal": order_items
                }
            }
            return data

        fm.create_record('web_find_asset_detail', fm_serializer(self))
        fm.logout()
        # print(fm_serializer(self))

        '''
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

        order.id_code = '921-' + generate_id_code()
        order.save()

        '''
        messages.success(self.request, 'Your order was successful!')
        return redirect('accounts:employee')
