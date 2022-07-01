from django.urls import path
from Blog import views

urlpatterns = [
    path('blog', views.blog, name='blog'),
]

