from django.urls import path
from .import views
from .views import root_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", root_view),
    path("api/home/", views.HomeView.as_view(), name="home"),
    path("api/about/", views.AboutView.as_view(), name="about"),
    path("api/testimonials/", views.TestimonailsView.as_view(), name="testimonials"),
    path("api/services/", views.ServicesView.as_view(), name="services"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
