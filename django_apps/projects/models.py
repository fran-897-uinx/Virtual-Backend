from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Project(models.Model):
    STATUS = [
        ("Not Started", "not_started"),
        ("In Progress", "in_progress"),
        ("Completed", "completed")
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    tech_stack = models.JSONField(blank=True, default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15, choices=STATUS, default="In Progress")
    version = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return f"{self.title} - {self.description}"

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="images")
    image = CloudinaryField("image")
    
    

class Certificate(models.Model):
    name = models.CharField(max_length=255)
    issuer = models.CharField(max_length=255)
    issue_date = models.DateField()
    certificate_image = CloudinaryField("image", blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.issuer} - {self.issue_date}"
