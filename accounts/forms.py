# Import forms
from django import forms
from django.forms import ModelForm
from allauth.account.forms import SignupForm
from crispy_forms.helper import FormHelper

from accounts.models import Shop, Employee
from django.contrib.auth.models import Group
from invitations.utils import get_invitation_model


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
    connects a user to an employee profile.
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


class InviteForm(forms.ModelForm):
    """
    A employee invite form.
    'supervisor' can invite employees to create an account.
    """
    helper = FormHelper()
    helper.form_show_labels = True

    class Meta:
        Invitation = get_invitation_model()
        model = Invitation
        fields = 'email', 'inviter'


'''
    def save(self, *args, **kwargs):
        cleaned_data = super(InvitationAdminAddForm, self).clean()
        phoneNumber = cleaned_data.get("phoneNumber")  <="NEW LINE"
        email = cleaned_data.get("email")
        params = {'email': email, 'phoneNumber': phoneNumber }  <="MADE CHANGES HERE"
        #rest of the function
    class Meta:
        model = Invitation
        fields = ("phoneNumber","email", "inviter")  <="MADE CHANGES HERE"

class InviteForm(forms.Form, CleanEmailMixin):
    phoneNumber = forms.CharField(max_length=30, required=True) <="NEW LINE"
    email = forms.EmailField(....)

    def save(self, email):
    #def save(self, email, phoneNumber): <="MADE CHANGES HERE"
        return Invitation.create(email=email)
        # return Invitation.create(email=email, phoneNumber=phoneNumber) <="MADE CHANGES HERE"
'''
