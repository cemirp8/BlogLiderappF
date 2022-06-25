from django.urls import path
from ContactApp import views


urlpatterns = [
    path('duda_estudiante', views.dudaestudiante, name='duda_estudiante'),
    path('interesado/', views.interesado, name='interesado'),
]

