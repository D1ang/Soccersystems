from .decorators import allowed_users
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from orders.models import Order
from decimal import Decimal


@login_required
@allowed_users(allowed_roles=['supervisor'])
def adminpage(request):
    """
    A view that displays the dashboard
    for the admin & paginate the order list.
    """
    return render(request, 'accounts/adminpage.html')


@login_required
@allowed_users(allowed_roles=['employee', 'admin'])
def customerpage(request):
    """
    A view that displays the dashboard
    for the employee & paginate the order list.
    The orders are shown on a shop based level.
    """
    order_list = request.user.employee.shop.order_set.all().order_by('-date')
    paginator = Paginator(order_list, 6)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    total_orders = order_list.count()
    pending_orders = order_list.filter(status='pending').count()
    finished_orders = order_list.filter(status='finished').count()

    context = {
        'page_object': page_object,
        'total_orders': total_orders,
        'pending_orders': pending_orders,
        'finished_orders': finished_orders,
    }
    return render(request, 'accounts/customerpage.html', context)


@login_required
@allowed_users(allowed_roles=['employee', 'supervisor', 'admin'])
def orderdetails(request, pk_order):
    """
    A orderdetail page for the customers and admin to view the selected
    order and be able to download the provided artwork.
    Extra security is provided to prevent URL snooping.
    """
    admin = request.user

    if admin.is_active and admin.is_superuser:
        order = Order.objects.get(id=pk_order)
        tax = order.get_total() * Decimal(21 / 100)
        total = order.get_total() + tax

        context = {
            'order': order,
            'tax': tax,
            'total': total
        }
        return render(request, 'accounts/orderdetails.html', context)

    else:
        try:
            order = Order.objects.get(id=pk_order, user=request.user)
            tax = order.get_total() * Decimal(21 / 100)
            total = order.get_total() + tax

            context = {
                'order': order,
                'tax': tax,
                'total': total
            }
            return render(request, 'accounts/orderdetails.html', context)
        except ObjectDoesNotExist:
            messages.error(request, 'This order is not available')
            return redirect('accounts:customerpage')