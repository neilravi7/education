from django.shortcuts import render
from django.http import HttpResponse
from .models import Gallery

# Create your views here.

home_response ="""
<h1> work in progress <h2>
<ul>
<li>
    <a href="/updates">NEWS</a>
        </li>
<li>
    <a href="/gallery">GALLERY</a>
</li>
<ul/>
"""

def home(request):
    return HttpResponse(home_response)

def gallery(request):
    gallery = Gallery.objects.all()
    return render(request, 'school_gallery/gallery.html',{"gallery":gallery})