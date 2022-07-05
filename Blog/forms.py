from django import forms

class Publicacion_Form(forms.Form):
    titulo= forms.CharField(max_length=1000)
    contenido= forms.CharField(max_length=1000, widget=forms.Textarea)