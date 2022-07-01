from django import forms

class Newsletter_formulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    pais=forms.CharField(max_length=50)

cursos=[('Curso 001', 'Inteligencia Emocional y Liderazgo'),
    ('Curso 002', 'Innovación y Creatividad Empresarial')
]

class Cursos_formulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    telefono=forms.IntegerField()    
    curso=forms.ChoiceField(choices=cursos, required=True, label='Selecciona el curso')