from django.contrib import admin
from .models import Gallery
# Register your models here.

@admin.register(Gallery)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ("id", "file", "uploaded_at")  # Display columns