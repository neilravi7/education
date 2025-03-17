from django.urls import path
from .views import home, gallery

app_name = 'school_gallery'

urlpatterns = [
    path('', home, name="home" ),
    path('gallery', gallery, name="gallery"),
]
