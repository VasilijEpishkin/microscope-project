from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Image
from .serializers import ImageSerializer

class GalleryView(TemplateView):
    template_name = 'gallery/gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = Image.objects.all()
        return context

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            return Response({'url_prefix': instance.url_prefix})
        except Image.DoesNotExist:
            return Response({"error": "Image not found"}, status=404)