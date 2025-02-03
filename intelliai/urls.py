"""
URL configuration for intelliai project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# project-level urls.py (usually in the project folder, e.g., intelliai/urls.py)
from operator import index
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from intelliweb import views  # Import the views module from your app


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('intelliweb.urls')),  # Routes to your app's URLs
    path('index/', views.index_view, name='index_view'),  # URL for index.html
    path('background/<int:project_id>/', views.background_image, name='background_image'),  # Directly map to the background_image view
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serve media files
