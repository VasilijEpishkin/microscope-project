# Generated by Django 4.2 on 2024-11-21 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='tile_overlap',
        ),
        migrations.RemoveField(
            model_name='image',
            name='tile_size',
        ),
    ]
