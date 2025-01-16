from django.shortcuts import render
from django.http import HttpResponse

def project_view(request):
    # Lazy import to avoid models being accessed before the app is ready
    from .models import Project

    # Fetch the project data, including related features and team members
    project = Project.objects.prefetch_related('features', 'team_members').first()

    # To render the title dynamically
    project_title = list("FINAL YEAR PROJECT 2025")

    # Pass the background image URL to the template
    return render(request, 'project.html', {
        'project': project,
        'features': project.features.all() if project else [],
        'team_members': project.team_members.all() if project else [],
        'project_title': project_title,
        'background_image_url': project.background_image.url if project and project.background_image else None,
    })

def background_image(request, project_id):
    from .models import Project
    try:
        project = Project.objects.get(id=project_id)
        if project.background_image:
            with open(project.background_image.path, 'rb') as f:
                return HttpResponse(f.read(), content_type='image/jpeg')
        else:
            return HttpResponse(status=404)  # Background image not set
    except Project.DoesNotExist:
        return HttpResponse(status=404)
