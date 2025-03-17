from django.urls import path
from .views import updates_and_news

app_name = "school_updates"

urlpatterns = [
    path('updates', updates_and_news, name="updates_and_news"),
]
