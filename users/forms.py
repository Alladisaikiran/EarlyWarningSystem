from django import forms
from .models import UserRegistrationModel


class UserRegistrationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'pattern': '[a-zA-Z]+'}), required=True, max_length=100)
    loginid = forms.CharField(widget=forms.TextInput(attrs={'pattern': '[a-zA-Z]+'}), required=True, max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'pattern': '(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}',
        'title': 'Must contain at least one number, one uppercase and one lowercase letter, and at least 8 characters'
    }), required=True, max_length=100)
    mobile = forms.CharField(widget=forms.TextInput(attrs={'pattern': '[56789][0-9]{9}'}), required=True, max_length=100)
    # Corrected email regex to ensure a proper domain is present
    email = forms.CharField(widget=forms.TextInput(attrs={
        'pattern': r'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$',
        'title': 'Enter a valid email address with a proper domain name (e.g., example@gmail.com)'
    }), required=True, max_length=100)
    locality = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 22}), required=True, max_length=250)
    city = forms.CharField(widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'pattern': '[A-Za-z ]+', 'title': 'Enter Characters Only '}
    ), required=True, max_length=100)
    state = forms.CharField(widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'pattern': '[A-Za-z ]+', 'title': 'Enter Characters Only '}
    ), required=True, max_length=100)
    status = forms.CharField(widget=forms.HiddenInput(), initial='waiting', max_length=100)

    class Meta:
        model = UserRegistrationModel
        fields = '__all__'












