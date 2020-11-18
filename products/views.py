from django.views.generic import ListView
from .models import ProductItem


class ItemListView(ListView):
    """
    Shows all the available products items
    on 1 page.
    """
    model = ProductItem
    template_name = 'products/items.html'
