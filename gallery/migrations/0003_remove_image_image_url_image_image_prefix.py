# Generated by Django 4.2 on 2024-11-28 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_remove_image_tile_overlap_remove_image_tile_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image_url',
        ),
        migrations.AddField(
            model_name='image',
            name='image_prefix',
            field=models.CharField(default='default', max_length=100),
        ),
    ]
