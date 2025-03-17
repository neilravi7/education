from django.db import models

class Notice(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    notice = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'notice'
        verbose_name = "Notice"
        verbose_name_plural = "Notices"  # Explicit plural form

    def __str__(self):
        return self.notice[:50]  # Display the first 50 characters
    

class Activities(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='activities/')
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'activities'
        verbose_name = "Activity"
        verbose_name_plural = "Activities"  # Explicit plural form

    def __str__(self):
        return self.title
    

class Circulars(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='circulars/')
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'circulars'
        verbose_name = "Circular"
        verbose_name_plural = "Circulars"  # Explicit plural form
        

    def __str__(self):  
        return self.title