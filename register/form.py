from django import forms
from django.contrib.auth.forms import UserCreationForm
from register.models import Account

class RegistrationForm(UserCreationForm):
    email=forms.EmailField(max_length=60,min_length=5,help_text='Required email. Add valid email')

    class Meta:
        model=Account
        fields=('email','username','first_name','last_name','password1','password2')
