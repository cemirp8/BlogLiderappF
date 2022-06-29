from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('registro_usuario/', views.registro_usuario, name='registro_usuario'),
]
