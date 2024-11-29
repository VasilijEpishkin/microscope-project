from django.db import models

class Image(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    title = models.CharField(max_length=200)
    url_prefix = models.CharField(max_length=100, default='default', unique=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']