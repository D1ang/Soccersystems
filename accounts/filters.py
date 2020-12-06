import django_filters as filters
from orders.models import Order
from django.forms.widgets import TextInput


class OrderFilter(filters.FilterSet):
    """
    Creating a filterset for the Order model.
    This will search through the Order model
    and filter out the request provided by the admin.
    """
    company = filters.CharFilter(
        field_name='user__customer__company_name',
        lookup_expr='icontains',
        widget=TextInput(attrs={'placeholder': 'Company name'})
    )
    status = filters.ChoiceFilter(
        choices=Order.STATUS,
        empty_label='Orderstatus'
    )
    start_date = filters.DateFilter(
        field_name='date',
        label='Date',
        lookup_expr='gte',
        widget=TextInput(
            attrs={'type': 'date', 'placeholder': 'Date from to today'}
        )
    )

    class Meta:
        model = Order
        fields = ['company', 'status', 'start_date']
