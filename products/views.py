from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import ProductGroup, ProductItem
from .filters import ItemFilter
from django.core.paginator import Paginator


@login_required
def products_list(request):
    """
    Shows all the available product
    groups and all available product items
    on 1 page.
    """

    product_list = ProductGroup.objects.all()
    product_item_list = ProductItem.objects.all()

    itemFilter = ItemFilter(request.GET, queryset=product_item_list)
    product_item_list = itemFilter.qs

    # Paginate the order to max 6 result per page
    paginator = Paginator(product_item_list, 15)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    context = {
        'product_list': product_list,
        'product_item_list': product_item_list,
        'page_object': page_object,
        'itemFilter': itemFilter,
    }
    return render(request, 'products/products.html', context)


@login_required
def product_items(request, pk_product):
    """
    A product items page for the employee
    to view and order articles.
    """

    product_item_list = ProductItem.objects.filter(product_group=pk_product)

    itemFilter = ItemFilter(request.GET, queryset=product_item_list)
    product_item_list = itemFilter.qs

    # Paginate the order to max 6 result per page
    paginator = Paginator(product_item_list, 15)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    context = {
        'product_item_list': product_item_list,
        'page_object': page_object,
        'itemFilter': itemFilter,
    }
    return render(request, 'products/product_items.html', context)
