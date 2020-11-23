from django.shortcuts import render
from .models import ProductGroup, ProductItem
from .filters import ItemFilter


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

    context = {
        'product_list': product_list,
        'product_item_list': product_item_list,
        'itemFilter': itemFilter,
    }

    return render(request, 'products/items.html', context)


def product_items(request, pk_product):
    """
    A product items page for the employee
    to view and order articles.
    """

    product_item_list = ProductItem.objects.filter(product_group=pk_product)

    context = {
        'product_item_list': product_item_list
    }

    return render(request, 'products/product_items.html', context)
