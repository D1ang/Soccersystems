import django_filters as filters
from orders.models import Order
from accounts.models import Shop
from django.forms.widgets import TextInput
from django.utils.translation import gettext_lazy as _


class OrderFilter(filters.FilterSet):
    '''
    Creating a filterset for the Order model.
    This will search through the Order model
    and filter out the request provided by the admin.
    '''
    shop = filters.ModelChoiceFilter(
        queryset=Shop.objects.all(),
        empty_label=_('Shop name')
    )
    status = filters.ChoiceFilter(
        choices=Order.STATUS,
        empty_label=_('Status')
    )
    delivery_date = filters.DateFilter(
        field_name='delivery_date',
        label='Date',
        lookup_expr='gte',
        widget=TextInput(
            attrs={'type': 'date', 'placeholder': 'Date from to today'}
        )
    )

    class Meta:
        model = Order
        fields = ['shop', 'status', 'delivery_date']
