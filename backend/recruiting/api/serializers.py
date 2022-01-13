from rest_framework.serializers import ModelSerializer
from recruiting.models import JobPosting


class JobPostingSerializer(ModelSerializer):
    class Meta:
        model = JobPosting
        fields = "__all__"
