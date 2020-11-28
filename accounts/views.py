from .decorators import allowed_users
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.paginator import Paginator


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
    """
    order_list = request.user.order_set.all().order_by('-date')
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
