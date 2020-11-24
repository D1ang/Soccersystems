from .decorators import allowed_users
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
@allowed_users(allowed_roles=['supervisor'])
def adminpage(request):
    """
    A view that displays the dashboard
    for the admin & paginate the order list.
    """

    return render(request, 'accounts/adminpage.html')


@login_required
@allowed_users(allowed_roles=['employee'])
def customerpage(request):
    """
    A view that displays the dashboard
    for the customer & paginate the order list.
    """

    return render(request, 'accounts/customerpage.html')
