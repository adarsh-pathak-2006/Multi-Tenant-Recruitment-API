from django import forms
from core.models import User


class RegisterForm(forms.Form):
    username=forms.CharField()
    role=forms.ChoiceField(choices=User.ROLE_CHOICES)
    password=forms.CharField(widget=forms.PasswordInput())
    rep_password=forms.CharField(widget=forms.PasswordInput()) 