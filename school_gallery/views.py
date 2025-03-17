from django.shortcuts import render
from django.http import HttpResponse
from .models import Gallery

# Create your views here.

def home(request):
    return HttpResponse("<h1> work in progress <h2>")

def gallery(request):
    gallery = Gallery.objects.all()
    return render(request, 'school_gallery/gallery.html',{"gallery":gallery})