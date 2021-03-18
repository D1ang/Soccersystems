import django_filters as filters
from products.models import ItemGroup, ProductItem
from django.forms.widgets import TextInput
from django.utils.translation import gettext_lazy as _


class ItemFilter(filters.FilterSet):
    '''
    Creating a filterset for the ProductItem model.
    This will search through the ProductItem model
    & filter out the request provided by the user.
    '''
    description = filters.CharFilter(
        lookup_expr='icontains',
        widget=TextInput(attrs={'placeholder': _('Article name')})
    )

    item_group = filters.ModelChoiceFilter(
        queryset=ItemGroup.objects.all(),
        empty_label=_('Group')
    )

    size = filters.CharFilter(
        lookup_expr='icontains',
        widget=TextInput(attrs={'placeholder': _('Size')})
    )

    class Meta:
        model = ProductItem
        fields = ['description', 'item_group', 'size']
