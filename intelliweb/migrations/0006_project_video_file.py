# Generated by Django 5.1.4 on 2025-02-03 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intelliweb', '0005_animal_technology'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
    ]
