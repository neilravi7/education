from django.shortcuts import render
from .models import Notice, Activities, Circulars

def updates_and_news(request):
    notices = Notice.objects.all()
    activities = Activities.objects.all()
    circulars = Circulars.objects.all()

    context = {
        "notices": notices,
        "activities": activities,
        "circulars": circulars
    }
    return render(request, "school_updates/updates.html", context)
