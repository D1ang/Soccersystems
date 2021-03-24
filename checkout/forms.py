from django import forms
from django.utils.translation import gettext_lazy as _


class CheckoutForm(forms.Form):
    '''
    A checkout form that collects the delivery date &
    comments provided by the user.
    '''
    comments = forms.CharField(
        required=False,
        max_length=250,
        label=_('Comments'),
        widget=forms.Textarea(attrs={'placeholder': _('max 250 characters')})
    )
    delivery_date = forms.DateField(
        required=True,
        label=_('Delivery date'),
        widget=forms.SelectDateWidget()
    )
