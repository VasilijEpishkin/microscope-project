from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from gallery.views import ImageViewSet, GalleryView

router = DefaultRouter()
router.register(r'images', ImageViewSet, basename='image')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', GalleryView.as_view(), name='gallery'),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)