from django import forms
from .models import Signup

class SignupForm(forms.ModelForm):
    class Meta:
        model=Signup
        fields=['email','full_name']

class ContactForm(forms.Form):
    email=forms.EmailField()
    name=forms.CharField()
    message=forms.CharField()