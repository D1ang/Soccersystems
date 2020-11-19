import django_filters as filters
from products.models import ProductItem


class ItemFilter(filters.FilterSet):
    """
    Creating a filterset for the ProductItem model.
    This will search through the ProductItem model
    and filter out the request provided by the user.
    """
    description = filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = ProductItem
        fields = ['price']
