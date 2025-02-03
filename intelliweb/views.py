from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, ExtensionSite, Animal, Technology

def project_view(request):
    """Renders the project page with project details, features, team members, extension site link, and video."""
    
    # Fetch the first available project
    project = Project.objects.prefetch_related('features', 'team_members').first()
    
    # Render the title dynamically
    project_title = list("FINAL YEAR PROJECT 2025")

    # Fetch extension site link (if available)
    extension_site = ExtensionSite.objects.first()

    # Fetch animals and technologies to pass to index.html content
    animals = Animal.objects.all()
    technologies = Technology.objects.all()

    # Fetch the video URL if the project has a video file
    video_url = project.video_file.url if project and project.video_file else None

    return render(request, 'project.html', {
        'project': project,
        'features': project.features.all() if project else [],
        'team_members': project.team_members.all() if project else [],
        'project_title': project_title,
        'background_image_url': project.background_image.url if project and project.background_image else None,
        'extension_site': extension_site,
        'animals': animals,  # Passed for index content
        'technologies': technologies,  # Passed for index content
        'video_url': video_url,  # Pass video URL to template
    })

def background_image(request, project_id):
    """Serves the background image dynamically for the project."""
    
    try:
        project = Project.objects.get(id=project_id)
        if project.background_image:
            with open(project.background_image.path, 'rb') as f:
                return HttpResponse(f.read(), content_type='image/jpeg')
        return HttpResponse(status=404)  # Background image not set
    except Project.DoesNotExist:
        return HttpResponse(status=404)

def index_view(request):
    """Renders the index page with animals and technologies."""
    
    animals = Animal.objects.all()
    technologies = Technology.objects.all()

    return render(request, 'index.html', {
        'animals': animals,
        'technologies': technologies,
    })
