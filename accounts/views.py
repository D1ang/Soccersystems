from .decorators import allowed_users
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.core.paginator import Paginator
from orders.models import Order
from .forms import EmployeeForm
from .filters import OrderFilter


@login_required
@allowed_users(allowed_roles=['admin'])
def admin(request):
    '''
    A view that displays the dashboard
    for the admin & paginate the order list.
    '''
    order_list = Order.objects.all().order_by('-date')
    total_orders = order_list.count()
    requests = order_list.filter(status='request').count()
    sent_orders = order_list.filter(status='sent').count()

    orderFilter = OrderFilter(request.GET, queryset=order_list)
    order_list = orderFilter.qs

    # Paginate the orders to max 10 results per page
    paginator = Paginator(order_list, 10)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    context = {
        'page_object': page_object,
        'total_orders': total_orders,
        'requests': requests,
        'sent_orders': sent_orders,
        'orderFilter': orderFilter,
    }
    return render(request, 'accounts/admin.html', context)


@login_required
@allowed_users(allowed_roles=['supervisor'])
def supervisor(request):
    '''
    A view that displays the dashboard
    for the supervisor & paginate the order list.
    '''
    order_list = Order.objects.all().order_by('-date')
    total_orders = order_list.count()
    pending_orders = order_list.filter(status='pending').count()
    finished_orders = order_list.filter(status='finished').count()

    orderFilter = OrderFilter(request.GET, queryset=order_list)
    order_list = orderFilter.qs

    # Paginate the orders to max 10 results per page
    paginator = Paginator(order_list, 10)
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
    '''
    A view that displays the dashboard
    for the employee & paginate the order list
    The orders are shown on a shop based level.
    '''
    order_list = request.user.employee.shop.order_set.all().order_by('-date')
    paginator = Paginator(order_list, 10)
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
def userprofile(request):
    '''
    Profile settings for the user,
    to change/update their own profile.
    '''
    employee = request.user.employee
    form = EmployeeForm(instance=employee)

    order_list = request.user.employee.shop.order_set.all().order_by('-date')
    total_orders = order_list.count()

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()

            message = _('Profile update successful')
            messages.info(request, message=message)

            # New users will be redirected to the services to start ordering.
            if total_orders < 1:
                return redirect('products:products')
            else:
                return redirect('accounts:employee')
    else:
        context = {'form': form}
        return render(request, 'accounts/userprofile.html', context)


@login_required
@allowed_users(allowed_roles=['employee', 'supervisor', 'admin'])
def orderdetails(request, pk_order):
    '''
    A orderdetail page for the employees &
    supervisor to view the selected order.
    Extra security is provided to prevent URL snooping.
    '''
    admin = request.user

    if admin.is_active and admin.is_superuser:
        order = Order.objects.get(id=pk_order)
        tax = order.get_total() / 100 * 21
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
            tax = order.get_total() / 100 * 21
            total = order.get_total() + tax

            context = {
                'order': order,
                'tax': tax,
                'total': total
            }
            return render(request, 'accounts/orderdetails.html', context)
        except ObjectDoesNotExist:
            message = _('This order has not yet been completed by a colleague')
            messages.error(request, message=message)
            return redirect('accounts:employee')
