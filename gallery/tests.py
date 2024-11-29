from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Image

class ImageModelTests(TestCase):
    def test_create_image(self):
        image = Image.objects.create(
            title="Test Image",
            image_url="/static/gallery/images/test.jpg",
            width=1024,
            height=768
        )
        self.assertEqual(image.title, "Test Image")
        self.assertEqual(image.get_dzi_url(), f"/static/tiles/{image.id}/images.dzi")
        self.assertEqual(image.width, 1024)
        self.assertEqual(image.height, 768)

class ImageAPITests(APITestCase):
    def setUp(self):
        self.image = Image.objects.create(
            title="Test Image",
            image_url="/static/gallery/images/test.jpg",
            width=1024,
            height=768
        )

    def test_list_images(self):
        response = self.client.get('/api/images/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)
        self.assertTrue('dzi_url' in response.data['results'][0])