# Generated by Django 5.0 on 2024-01-05 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FrontendApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignUpDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.EmailField(blank=True, max_length=100, null=True)),
                ('Password', models.CharField(blank=True, max_length=100, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='Profile Image1')),
            ],
        ),
    ]