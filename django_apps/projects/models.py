from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Project(models.Model):

    STATUS = [
        ("not_started", "Not Started"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()

    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)

    tech_stack = models.JSONField(blank=True, default=list)

    colaborators = models.JSONField(blank=True, default=list)

    state = models.CharField(max_length=20, choices=STATUS, default="not_started")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="images"
    )

    image = CloudinaryField("image")

    def __str__(self):
        return f"{self.project.title} image"
    

class Certificate(models.Model):
    name = models.CharField(max_length=255)
    issuer = models.CharField(max_length=255)
    issue_date = models.DateField()
    certificate_image = CloudinaryField("image", blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.issuer} - {self.issue_date}"
