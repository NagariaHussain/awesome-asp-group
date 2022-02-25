from rest_framework.serializers import ModelSerializer
from recruiting.models import JobPosting, Profile
from django.contrib.auth import models as auth_models
from recruiting.models import JobApplication


class JobPostingSerializer(ModelSerializer):
    class Meta:
        model = JobPosting
        fields = [
            "id",
            "job_title",
            "description",
            "is_published",
            "location",
            "created_at",
            "department",
        ]

    def create(self, validated_data):
        return JobPosting.objects.create(**validated_data)


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ["user_type"]


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = auth_models.User
        fields = ["username", "first_name", "last_name", "email", "profile"]


class ApplicationSerializer(ModelSerializer):
    class Meta:
        model = JobApplication
        fields = "__all__"
