from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django import forms
from .models import Employee


class MyCustomSignupForm(SignupForm):
    """
    Extend the allauth register form and
    connects an user to a employee profile.
    """
    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['shop'] = forms.CharField(widget=forms.TextInput(
            attrs={'placeholder': 'Shop'}), required=True)

    def save(self, request):
        shop = self.cleaned_data.pop('shop')
        user = super(MyCustomSignupForm, self).save(request)

        group = Group.objects.get(name='employee')
        user.groups.add(group)

        if request.method == 'POST':
            # connect the employee to an user @ creation.
            Employee.objects.create(
                user=user,
                email=user.email,
                shop=shop,
            )
        return user
