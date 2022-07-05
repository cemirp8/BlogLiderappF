from django import forms
from django.contrib.auth.models import User

class PublicacionForm(forms.Form):
    titulo= forms.CharField()
    contenido= forms.CharField(max_length=1000, widget=forms.Textarea)

    class Meta:
        fields = ('titulo', 'contenido')
