from django.shortcuts import render
from django.http import JsonResponse
from .models import Project, Certificate
from rest_framework import generics
from .serializers import ProjectSerializer, CertificateSerializer

# Create your views here.


class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetailView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = "id"   # use ID in the URL


class CertificateListView(generics.ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class CertificateDetailView(generics.RetrieveAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    lookup_field = "id"  # use ID in the URL
