from django import forms
from .file_widgets import CustomClearableFileInput
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget  # noqa: F401


class CheckoutForm(forms.Form):
    """
    A checkout form that collects the customer
    Billing address and artwork upload.
    """
    company_name = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    street_address = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '1234 Main street'})
    )
    address_line_2 = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Appartment or floor'})
    )
    city = forms.CharField()
    region = forms.CharField(
        required=False,
        label='Province/region'
    )
    postal = forms.CharField()
    country = CountryField(blank_label='Select country').formfield()
    artwork = forms.FileField(
        required=True,
        widget=CustomClearableFileInput
    )
    comments = forms.CharField(
        required=False,
        max_length=250,
        widget=forms.Textarea(attrs={'placeholder': 'max 250 characters'})
    )