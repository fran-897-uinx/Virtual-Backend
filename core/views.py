from rest_framework import generics
from django.http import JsonResponse
from .models import Home, About,Testimonails,Service
from .serializers import HomeSerializer, AboutSerializer,TestimonySerializer,ServicesSerializer

class HomeView(generics.ListAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer


class AboutView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class TestimonailsView(generics.ListAPIView):
    queryset = Testimonails.objects.all()
    serializer_class = TestimonySerializer


class ServicesView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServicesSerializer


def root_view(request):
    return JsonResponse({"status": "ok", "message": "Backend is running"})
