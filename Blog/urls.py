from django.urls import path
from Blog import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('categoria/<int:categoria_id>/', views.categoria, name='categoria')
]

