from django.shortcuts import render


def products(request):
    """
    Products index page
    """

    return render(request, 'products/index.html')
