from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    mentor = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    college = models.CharField(max_length=255)
    background_image = models.ImageField(upload_to='backgrounds/', null=True, blank=True)  # Field for background image

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

    def __str__(self):
        return self.name
