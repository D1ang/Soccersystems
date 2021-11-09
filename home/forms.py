from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3
from django.utils.translation import gettext as _


class ContactForm(forms.Form):
    contact_name = forms.CharField(
        label=_('Name'),
        required=True,
        max_length=50,
    )
    contact_email = forms.EmailField(
        label=_('Email'),
        required=True,
        max_length=150,
    )
    content = forms.CharField(
        label=_('Message'),
        required=True,
        max_length=250,
        widget=forms.Textarea(attrs={'rows': 4})
    )
    captcha = ReCaptchaField(
        widget=ReCaptchaV3(attrs={'required_score':0.75}),
    )
