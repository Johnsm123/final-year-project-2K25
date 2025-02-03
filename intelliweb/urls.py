from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import project_view, index_view, background_image

urlpatterns = [
    path('', project_view, name='project_view'),  # Main project page (project.html)
    path('index/', index_view, name='index_view'),  # URL for index.html
    path('background/<int:project_id>/', background_image, name='background_image'),  # Dynamic background image
]

# Serve media files (like videos) in development (when DEBUG is True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
