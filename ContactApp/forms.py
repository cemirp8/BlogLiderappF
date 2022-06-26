from django import forms

class DudaEstudianteFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    mensaje= forms.CharField(max_length=200, widget=forms.Textarea)


class InteresadoFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    email= forms.EmailField()
    telefono= forms.IntegerField()
    curso_de_interes= forms.CharField(max_length=30)