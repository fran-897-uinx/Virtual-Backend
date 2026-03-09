from django.contrib import admin
from django_apps.projects.models import ProjectImage
from .models import Project, Certificate


# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','github_link')
    list_filter = ("title",)
    search_fields = ['title', 'description']

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ("project",)
    list_filter = ("project",)
    search_fields = ("project",)
    
    
@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("name", "issuer", "issue_date")
    list_filter = ("issuer",)
    search_fields = ["name", "issuer"]
