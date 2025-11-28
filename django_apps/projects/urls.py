from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProjectListView.as_view(), name="project-list"),
    path("<int:id>/", views.ProjectDetailView.as_view(), name="project-detail"),
    path("certificates/", views.CertificateListView.as_view(), name="certificate-list"),
    path(
        "certificates/<int:id>/",
        views.CertificateDetailView.as_view(),
        name="certificate-detail",
    ),
]
