from rest_framework.serializers import (
    ModelSerializer,
    ReadOnlyField,
    CharField,
    Serializer,
)
from recruiting.models import JobPosting, Profile
from recruiting.models.interview import (
    InterviewRound,
    InterviewEvent,
    InterviewFileAttachment,
    Communication,
    InterviewRoundAssignment,
    InterviewRoundAssignmentEvent,
)
from django.contrib.auth import models as auth_models
from recruiting.models import JobApplication


class JobPostingSerializer(ModelSerializer):
    class Meta:
        model = JobPosting
        company_name = ReadOnlyField(source="company.name")
        fields = [
            "id",
            "job_title",
            "description",
            "is_published",
            "location",
            "created_at",
            "company_name",
            "department",
        ]

    def create(self, validated_data):
        return JobPosting.objects.create(**validated_data)


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ["user_type", "avatar_image"]


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = auth_models.User
        fields = ["username", "first_name", "last_name", "email", "profile"]


class ApplicationSerializer(ModelSerializer):
    class Meta:
        model = JobApplication
        fields = "__all__"


# Interview Related Serializers


class CommentSerializer(Serializer):
    comment = CharField(max_length=500)


class InterviewRoundSerializer(ModelSerializer):
    class Meta:
        model = InterviewRound
        fields = ("id", "index", "status", "name")


class CommunicationSerializer(ModelSerializer):
    sender = UserSerializer(read_only=True)

    class Meta:
        model = Communication
        fields = ("body", "sender")


class InterviewFileAttachmentSerializer(ModelSerializer):
    class Meta:
        model = InterviewFileAttachment
        fields = ("id", "file")


class InterviewRoundAssignmentSerializer(ModelSerializer):
    assignee = UserSerializer(read_only=True)

    class Meta:
        model = InterviewRoundAssignment
        fields = ("id", "assignee")


class InterviewRoundAssignmentEventSerializer(ModelSerializer):
    assignment = InterviewRoundAssignmentSerializer()

    class Meta:
        model = InterviewRoundAssignmentEvent
        fields = ["assignment"]


class InterviewEventSerializer(ModelSerializer):
    communication = CommunicationSerializer()
    attachment = InterviewFileAttachmentSerializer()
    assignment_event = InterviewRoundAssignmentEventSerializer()

    class Meta:
        model = InterviewEvent
        fields = (
            "id",
            "type",
            "created_at",
            "communication",
            "attachment",
            "assignment_event",
        )
