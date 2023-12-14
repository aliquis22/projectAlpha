from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Customer, Organisation
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class OrganisationForm(forms.ModelForm):
    class Meta:
        model = Organisation
        fields = ['name', 'email', 'address', 'tables', 'working_hours', 'cuisine']

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = Customer
