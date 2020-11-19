from django.shortcuts import render
from .models import ProductItem
from .filters import ItemFilter


def product_items_list(request):
    """
    Shows all the available products items
    on 1 page.
    """

    item_list = ProductItem.objects.all()

    itemFilter = ItemFilter(request.GET, queryset=item_list)
    item_list = itemFilter.qs

    context = {
       'item_list': item_list,
       'itemFilter': itemFilter,
    }

    return render(request, 'products/items.html', context)
