from django import forms
from .models import ContactMessage
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class SigninForm(AuthenticationForm):
    pass
