# Generated by Django 5.0 on 2023-12-11 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackendApp', '0002_productdb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productdb',
            old_name='Image',
            new_name='Image1',
        ),
        migrations.AddField(
            model_name='productdb',
            name='Image2',
            field=models.ImageField(blank=True, null=True, upload_to='Product'),
        ),
        migrations.AddField(
            model_name='productdb',
            name='Image3',
            field=models.ImageField(blank=True, null=True, upload_to='Product'),
        ),
    ]
