from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    tech_stack = models.CharField(max_length=200)
    live_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.description} - {self.image} - {self.github_link} - {self.tech_stack} - {self.live_link} - {self.created_at}"


class Certificate(models.Model):
    certificate_image = models.ImageField(
        upload_to="certificates/", blank=True, null=True
    )
    name = models.CharField(max_length=255)
    issuer = models.CharField(max_length=255)
    issue_date = models.DateField()
    certificate_image = models.ImageField(
        upload_to="certificates/", blank=True, null=True
    )

    def __str__(self):
        return f"{self.name} - {self.issuer} - {self.issue_date}"
