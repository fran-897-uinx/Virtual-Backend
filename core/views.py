from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Home, About, Service, Testimonails
from .serializers import (
    HomeSerializer,
    AboutSerializer,
    ServicesSerializer,
    TestimonialSerializer,
)


def root_view(request):
    return JsonResponse({"status": "ok", "message": "Backend is running"})


class HomeAPI(APIView):
    def get(self, request):
        home = Home.objects.all()
        serializer = HomeSerializer(home, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class AboutAPI(APIView):
    def get(self, request):
        about = About.objects.all()
        serializer = AboutSerializer(about, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ServicesAPI(APIView):
    def get(self, request):
        services = Service.objects.all()
        serializer = ServicesSerializer(
            services, many=True, context={"request": request}
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class TestimonialsAPI(APIView):
    def get(self, request):
        testimonials = Testimonails.objects.all()
        serializer = TestimonialSerializer(
            testimonials, many=True, context={"request": request}
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
