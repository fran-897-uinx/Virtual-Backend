from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
from .views import TestimonialsAPI

router = DefaultRouter()
router.register(r'api/testimonials', TestimonialsAPI, basename='testimonials')

urlpatterns = [
    path("", views.root_view),
    path("api/home/", views.HomeAPI.as_view(), name="home"),
    path("api/about/", views.AboutAPI.as_view(), name="about"),
    path("api/services/", views.ServicesAPI.as_view(), name="services"),
]

# add router urls
urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)