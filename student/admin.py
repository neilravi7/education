from django.contrib import admin
from .models import Student, TransferCertificate

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'admission_number', 'date_of_admission']
    search_fields = ['first_name', 'last_name', 'admission_number']
    ordering = ['-date_of_admission']

@admin.register(TransferCertificate)
class TransferCertificateAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'issued_date']
    search_fields = ['student__admission_number']
    ordering = ['-issued_date']
