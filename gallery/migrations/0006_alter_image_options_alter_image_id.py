# Generated by Django 4.2 on 2024-11-29 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_alter_image_options_remove_image_created_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]