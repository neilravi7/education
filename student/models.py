from django.db import models
from django.utils.timezone import now

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    admission_number = models.CharField(max_length=10, unique=True, blank=True)
    date_of_admission = models.DateField(auto_now_add=True)


    class Meta:
        db_table = 'students'

    def save(self, *args, **kwargs):
        if not self.admission_number:
            year = now().year  # Current Year
            last_student = Student.objects.filter(admission_number__startswith=str(year)).order_by('-admission_number').first()

            last_number = int(last_student.admission_number[-4:]) + 1 if last_student else 1
            self.admission_number = f"{year}{last_number:04d}"  # Format: 20250001, 20250002

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} - {self.admission_number}"

class TransferCertificate(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='transfer_certificate')
    tc_file = models.FileField(upload_to='transfer_certificates/')
    issued_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'transfer_certificates'

    def __str__(self):
        return f"TC - {self.student.first_name} {self.student.last_name}"