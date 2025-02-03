from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    mentor = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    college = models.CharField(max_length=255)
    background_image = models.ImageField(upload_to='backgrounds/', null=True, blank=True)  # Field for background image
    video_file = models.FileField(upload_to='videos/', null=True, blank=True)  # Field for video upload

    def __str__(self):
        return self.name

class Feature(models.Model):
    project = models.ForeignKey(Project, related_name='features', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    link = models.URLField()
    image_url = models.URLField()
    css_id = models.CharField(max_length=50)

class TeamMember(models.Model):
    project = models.ForeignKey(Project, related_name='team_members', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

class Destination(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class ExtensionSite(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the extension site")
    link = models.URLField(help_text="Enter the URL of the extension site")

    def __str__(self):
        return self.name

class Technology(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='technologies/')

class Animal(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='animals/')
