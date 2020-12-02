from django.contrib.auth.models import Group
from .models import Shop, Employee
from django import forms
from allauth.account.forms import SignupForm


class MyCustomSignupForm(SignupForm):
    """
    Extend the allauth register form and
    connects an user to a employee profile.
    """
    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['shop'] = forms.ModelChoiceField(queryset=Shop.objects.all(), required=True)
        self.fields['first_name'] = forms.CharField(max_length=50, required=True)
        self.fields['last_name'] = forms.CharField(max_length=50, required=True)

    def save(self, request):
        shop = self.cleaned_data.pop('shop')
        user = super(MyCustomSignupForm, self).save(request)
        first_name = self.cleaned_data.pop('first_name')
        last_name = self.cleaned_data.pop('last_name')
        group = Group.objects.get(name='employee')
        user.groups.add(group)

        if request.method == 'POST':
            # connect the employee to an user @ creation.
            Employee.objects.create(
                user=user,
                email=user.email,
                shop=shop,
                first_name=first_name,
                last_name=last_name
            )
        return user
