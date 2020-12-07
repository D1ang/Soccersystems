import django_filters as filters
from products.models import ItemGroup, ProductItem
from django.forms.widgets import TextInput


class ItemFilter(filters.FilterSet):
    """
    Creating a filterset for the ProductItem model.
    This will search through the ProductItem model
    and filter out the request provided by the user.
    """
    description = filters.CharFilter(
        lookup_expr='icontains',
        widget=TextInput(attrs={'placeholder': 'Article name'})
    )

    item_group = filters.ModelChoiceFilter(
        queryset=ItemGroup.objects.all(),
        empty_label=('Group')
    )

    size = filters.CharFilter(
        lookup_expr='icontains',
        widget=TextInput(attrs={'placeholder': 'Size'})
    )

    class Meta:
        model = ProductItem
        fields = ['description', 'item_group', 'size']
