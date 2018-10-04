from django.db import models
import os
# Create your models here.
class ImageDisplay(models.Model):

    title = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    Img = models.ImageField(upload_to='images/Home/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)
    Display = models.BooleanField(default=False)
    def __str__(self):
        return self.title