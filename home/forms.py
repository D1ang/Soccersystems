from django import forms
from django.utils.translation import gettext as _


class ContactForm(forms.Form):
    contact_name = forms.CharField(
        label=_('Name'),
        required=True
    )
    contact_email = forms.EmailField(
        label=_('Email'),
        required=True
    )
    content = forms.CharField(
        label=_('Message'),
        required=True,
        max_length=250,
        widget=forms.Textarea(attrs={'rows': 4})
    )
