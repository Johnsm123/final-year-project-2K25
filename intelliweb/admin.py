from django.contrib import admin
from .models import Project, Feature, TeamMember, Destination, ExtensionSite, Technology, Animal

# Register ExtensionSite directly
admin.site.register(ExtensionSite)

# Register Project with Custom Admin
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'mentor', 'department', 'college', 'video_file')  # Add 'video_file' to display
    search_fields = ('name', 'mentor', 'department')  # Enable search
    list_filter = ('department',)  # Add filters

    # Optional: If you want to show the video file in the form for admin
    fields = ('name', 'mentor', 'department', 'college', 'background_image', 'video_file')  # Add 'video_file' to fields

# Register Feature with Custom Admin
@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'project')
    search_fields = ('name', 'project__name')

# Register TeamMember with Custom Admin
@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'project')
    search_fields = ('name', 'project__name')

# Register Destination with Custom Admin
@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Register Technology Model
@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Register Animal Model
@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
