# forms.py
from django import forms
from .models import FancyPhoneNumber
from django.contrib.auth.forms import AuthenticationForm

class FancyPhoneNumberForm(forms.ModelForm):
    class Meta:
        model = FancyPhoneNumber
        fields = ['number', 'amount']  # Include the price_range field



class AdminLoginForm(AuthenticationForm):
    pass
