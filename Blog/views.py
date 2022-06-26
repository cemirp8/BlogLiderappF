from django.http import HttpResponse
from django.shortcuts import render
from Blog.models import *

def servicios(request):
    return render(request, "Blog/blog.html")
