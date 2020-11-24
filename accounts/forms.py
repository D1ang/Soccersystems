from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django import forms
from .models import Customer


class MyCustomSignupForm(SignupForm):
    """
    Extend the allauth register form and
    connects an user to a employee profile.
    """
    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['company_name'] = forms.CharField(widget=forms.TextInput(
            attrs={'placeholder': 'Company name'}), required=True)

    def save(self, request):
        company_name = self.cleaned_data.pop('company_name')
        user = super(MyCustomSignupForm, self).save(request)

        group = Group.objects.get(name='customer')
        user.groups.add(group)

        if request.method == 'POST':
            # connect the customer to an user @ creation.
            Customer.objects.create(
                user=user,
                email=user.email,
                company_name=company_name,
            )
        return user
