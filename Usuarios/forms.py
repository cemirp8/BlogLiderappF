import email
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    email = forms.EmailField(required=True)
    password1: forms.CharField(label="Contraseña", widget=forms.PasswordInput, help_text=None)
    password2: forms.CharField(label="Confirma la contraseña", widget=forms.PasswordInput, help_text=None)

    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2', 'first_name', 'last_name')
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    email = forms.EmailField(required=True)
    password1: forms.CharField(label="Contraseña", widget=forms.PasswordInput, required=False)
    password2: forms.CharField(label="Confirma la contraseña", widget=forms.PasswordInput, help_text=None, required=False)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name')
        help_texts = {k:"" for k in fields}
    

