from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .models import OrderItem, Order
from products.models import ProductItem as Item
from decimal import Decimal


class OrderSummaryView(LoginRequiredMixin, View):
    """
    A cart that shows the ordered product items and
    precalculates the totals, including tax.
    When cart is zero or no active order a warning
    message will be shown to the user.
    """
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            tax = order.get_total() * Decimal(21 / 100)
            total = order.get_total() + tax

            if total < 0:  # <------ Change this back to 1, when finished
                messages.warning(self.request, 'There is no active order')
                return redirect('/products')
            else:
                context = {
                    'object': order,
                    'tax': tax,
                    'total': total
                }
                return render(self.request, 'orders/cart.html', context)

        except ObjectDoesNotExist:
            messages.warning(self.request, 'There is no active order')
            return redirect('products:products')


def add_to_cart(request, slug):
    """
    Adds an item to the cart, creates an order &
    checks if an item already is in the order.
    """
    if request.user.is_anonymous:
        messages.add_message(request, messages.INFO, 'Please login to order')
        return redirect('products:products')  # <------- !NOTE change this to the login page
    else:
        shop = request.user.employee.shop
        item = get_object_or_404(Item, slug=slug)

        order_item, created = OrderItem.objects.get_or_create(
            item=item,
            price=item.price,
            article_id=item.article_id,
            user=request.user,
            shop=shop,
            quantity=request.GET.get('qty'),
            ordered=False,
        )
        order_querySet = Order.objects.filter(user=request.user, ordered=False)
        if order_querySet.exists():
            order = order_querySet[0]

            # check if the order item is in the order
            if order.items.filter(item__slug=item.slug).exists():
                messages.error(request, 'Item is already added')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                order.items.add(order_item)
                item.save()
                messages.info(request, 'Item is added to the cart')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            order = Order.objects.create(user=request.user, shop=shop)
            order.items.add(order_item)
            messages.info(request, 'Item is added to the cart')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_from_cart(request, slug):
    """
    Checks if the item is in the cart
    and removes it if there is an active order.
    """
    item = get_object_or_404(Item, slug=slug)
    order_querySet = Order.objects.filter(user=request.user, ordered=False)
    if order_querySet.exists():
        order = order_querySet[0]

        # check if the item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]

            order_item.delete()
            item.save()

            messages.info(request, 'Item removed from order')
            return redirect('orders:cart')
        else:
            messages.info(request, 'Item not in your order')
            return redirect('orders:cart')
    else:
        messages.info(request, 'There is\'nt an active order')
        return redirect('orders:cart')
