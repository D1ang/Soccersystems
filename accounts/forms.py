# Import forms
from accounts.models import Shop, Employee
from django.contrib.auth.models import Group
from django import forms
from django.forms import ModelForm
from allauth.account.forms import SignupForm


class EmployeeForm(ModelForm):
    """
    An employee edit profile form.
    'user' is excluded to probhit username edditing.
    'shop' is excluded to probhit shop edditing by employees.
    """
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['user', 'shop']


class MyCustomSignupForm(SignupForm):
    """
    Extends the allauth register form and
    connects an user to an employee profile.
    """
    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['shop'] = forms.ModelChoiceField(
            queryset=Shop.objects.all(), required=True)
        self.fields['first_name'] = forms.CharField(
            max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Firstname'}))
        self.fields['last_name'] = forms.CharField(
            max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Lastname'}))

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
