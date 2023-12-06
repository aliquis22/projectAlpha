from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Customer, Organisation

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Customer
        fields = ['username', 'email', 'password1', 'password2']

class OrganisationRegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    class Meta:
        model = Organisation
        fields = ['name', 'email', 'address','tables','working_hours','cuisine', 'password1', 'password2']