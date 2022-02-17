from rest_framework.serializers import ModelSerializer
from recruiting.models import JobPosting, Profile
from django.contrib.auth import models as auth_models


class JobPostingSerializer(ModelSerializer):
    class Meta:
        model = JobPosting
        fields = "__all__"


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ["user_type"]


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = auth_models.User
        fields = ["username", "first_name", "last_name", "email", "profile"]
