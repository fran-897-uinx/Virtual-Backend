from rest_framework import generics, parsers
from django.http import JsonResponse
from .models import Home, About,Testimonails,Service
from .serializers import (
    HomeSerializer,
    AboutSerializer,
    TestimonialSerializer,
    ServicesSerializer,
)

class HomeView(generics.ListAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]


class AboutView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

class TestimonailsView(generics.ListAPIView):
    queryset = Testimonails.objects.all()
    serializer_class = TestimonialSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

class ServicesView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServicesSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]


def root_view(request):
    return JsonResponse({"status": "ok", "message": "Backend is running"})
