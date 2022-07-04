from django import forms
from django.contrib.auth.models import User
from models import Categoria, categoria

class PublicacionForm(forms.Form):
    titulo= forms.CharField(max_length=40)
    autor= forms.ForeignKey(User, on_delete=forms.CASCADE)
    creado= forms.DateTimeField(auto_now_add=True)
    categoria= forms.CharField(label='Busqueda por categoría', widget=forms.Select(choices=categoria))

    class Meta:
        fields = ('titulo', 'autor', 'creado', 'categoria')
