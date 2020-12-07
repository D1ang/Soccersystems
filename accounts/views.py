from .decorators import allowed_users
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from orders.models import Order
from .forms import InviteForm
from .filters import OrderFilter
from decimal import Decimal
from invitations.utils import get_invitation_model


@login_required
@allowed_users(allowed_roles=['supervisor', 'admin'])
def supervisor(request):
    """
    A view that displays the dashboard
    for the supervisor & paginate the order list.
    """
    order_list = Order.objects.all().order_by('-date')
    total_orders = order_list.count()
    pending_orders = order_list.filter(status='pending').count()
    finished_orders = order_list.filter(status='finished').count()

    orderFilter = OrderFilter(request.GET, queryset=order_list)
    order_list = orderFilter.qs

    # Paginate the order to max 6 result per page
    paginator = Paginator(order_list, 6)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    context = {
        'page_object': page_object,
        'total_orders': total_orders,
        'pending_orders': pending_orders,
        'finished_orders': finished_orders,
        'orderFilter': orderFilter,
    }
    return render(request, 'accounts/supervisor.html', context)


@login_required
@allowed_users(allowed_roles=['employee'])
def employee(request):
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
    return render(request, 'accounts/dashboard.html', context)


@login_required
@allowed_users(allowed_roles=['employee', 'supervisor', 'admin'])
def orderdetails(request, pk_order):
    """
    A orderdetail page for the employees and supervisor to
    view the selected order.
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


def invite(request):
    """
    An invite page for the supervisor to invite employees
    to register their account.
    """
    form = InviteForm()
    context = {'form': form}

    return render(request, 'accounts/invite.html', context)
