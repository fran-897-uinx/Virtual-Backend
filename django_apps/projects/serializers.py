from rest_framework import serializers
from .models import Project, Certificate


class AbsoluteURLMixin:
    def get_absolute_image_url(self, request, image_field):
        if image_field and hasattr(image_field, "url"):
            return request.build_absolute_uri(image_field.url)
        return None


class ProjectSerializer(serializers.ModelSerializer, AbsoluteURLMixin):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get("request")
        return self.get_absolute_image_url(request, obj.image)


class CertificateSerializer(serializers.ModelSerializer, AbsoluteURLMixin):
    certificate_image = serializers.SerializerMethodField()

    class Meta:
        model = Certificate
        fields = "__all__"

    def get_certificate_image(self, obj):
        request = self.context.get("request")
        return self.get_absolute_image_url(request, obj.certificate_image)
