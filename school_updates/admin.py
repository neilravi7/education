from django.contrib import admin
from .models import Notice, Activities, Circulars

admin.site.site_header = "School Management Admin"
admin.site.site_title = "School Admin Portal"
admin.site.index_title = "Welcome to School Updates Admin"

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ("id", "notice", "created_at")  # Display columns
    search_fields = ("notice",)  # Search functionality
    list_filter = ("created_at",)  # Filter options
    ordering = ("-created_at",)  # Order by newest first

@admin.register(Activities)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "image", "created_at")
    search_fields = ("title",)
    list_filter = ("created_at",)
    ordering = ("-created_at",)

@admin.register(Circulars)
class CircularAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "image", "created_at")
    search_fields = ("title",)
    list_filter = ("created_at",)
    ordering = ("-created_at",)
