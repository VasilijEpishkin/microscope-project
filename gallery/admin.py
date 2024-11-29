from django.contrib import admin
from .models import Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'url_prefix')
    search_fields = ('title', 'url_prefix')