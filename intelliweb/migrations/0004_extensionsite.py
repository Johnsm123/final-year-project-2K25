# Generated by Django 5.1.4 on 2025-02-02 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intelliweb', '0003_project_background_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtensionSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the extension site', max_length=200)),
                ('link', models.URLField(help_text='Enter the URL of the extension site')),
            ],
        ),
    ]
