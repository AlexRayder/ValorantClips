from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=350)
    video_file = models.FileField(upload_to='videos/')
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)  # Agregar campo thumbnail
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
