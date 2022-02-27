from rest_framework.serializers import ModelSerializer
from .models import UserProfile
from .models import UserAppliedJob


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class UserAppliedJobSerializer(ModelSerializer):
    class Meta:
        model = UserAppliedJob
        fields = "__all__"
