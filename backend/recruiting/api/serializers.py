from rest_framework.serializers import ModelSerializer
from recruiting.models import JobPosting
from django.contrib.auth import models as auth_models
from recruiting.models import JobApplication

class JobPostingSerializer(ModelSerializer):
    class Meta:
        model = JobPosting
        fields = "__all__"


class UserSerializer(ModelSerializer):
    class Meta:
        model = auth_models.User
        fields = ["username", "first_name", "last_name", "email"]

class ApplicationSerializer(ModelSerializer):
    class Meta:
        model = JobApplication
        fields = "__all__"