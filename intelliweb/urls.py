# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_view, name='project_view'),  # Correct view mapping
]
