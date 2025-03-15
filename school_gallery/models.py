from django.db import models

class Gallery(models.Model):
    file = models.FileField(upload_to="gallery/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'gallery'
        verbose_name = "Gallery"
        verbose_name_plural = "Gallery"

    def __str__(self):
        return self.file.name[:20]