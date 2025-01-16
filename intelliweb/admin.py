from django.contrib import admin
from .models import Project, Feature, TeamMember, Destination

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'mentor', 'department', 'college')

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'project')

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'project')

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name',)
