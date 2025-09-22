from django.urls import path
from .import views
from .views import root_view


urlpatterns = [
    path("", root_view),
    path("api/home/", views.HomeView.as_view(), name="home"),
    path("api/about/", views.AboutView.as_view(), name="about"),
    path("api/testimonials/", views.TestimonailsView.as_view(), name="testimonials"),
    path("api/services/", views.ServicesView.as_view(), name="services"),
]
