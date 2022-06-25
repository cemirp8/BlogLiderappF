from django.db import models

# Create your models here.
class DudaEstudiante(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    mensaje= models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.nombre+" "+str(self.email)

class Interesado(models.Model):
    nombre= models.CharField(max_length=30)
    email= models.EmailField()
    telefono= models.IntegerField()
    curso_de_interes= models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.nombre+" "+str(self.curso_de_interes)

