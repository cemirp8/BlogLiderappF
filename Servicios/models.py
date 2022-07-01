from msilib.schema import Class
from tkinter import Widget
from django.db import models

# Create your models here.

class Newsletter(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    pais=models.CharField(max_length=50)

class Cursos(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    telefono=models.IntegerField()    
    curso=models.CharField(max_length=30)