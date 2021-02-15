from django import forms


class CheckoutForm(forms.Form):
    """
    A checkout form that collects the customer
    Billing address and artwork upload.
    """
    comments = forms.CharField(
        required=False,
        max_length=250,
        widget=forms.Textarea(attrs={'placeholder': 'max 250 characters'})
    )
    delivery_date = forms.DateField(
        required=True,
        widget=forms.SelectDateWidget()
    )
