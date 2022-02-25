import logging
import json

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserProfileSerializer
from .models import UserProfile

logger = logging.getLogger(__name__)


@api_view(["GET"])
def get_profile(request, username):
    """
    Get user profile by id (segment)
    """
    try:
        # profile = UserProfile.objects.get(pk=id)
        profile = UserProfile.objects.get(username=username)
    except UserProfile.DoesNotExist:
        return Response(404)

    serializer = UserProfileSerializer(profile)
    return Response(serializer.data, 200)


@api_view(["POST", "PUT"])
def save_profile(request):
    """
    Save user profile
    """

    if request.method == "POST":
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(201)
        return Response(serializer.errors, 400)

    if request.method == "PUT":
        data = json.loads(request.body)
        profile = UserProfile.objects.get(username=data['username'])

        profile.title = data['title']
        profile.age = data['age']
        profile.gender = data['gender']
        profile.location = data['location']
        profile.desired_location = data['desired_location']
        profile.desired_salary = data['desired_salary']
        profile.about = data['about']
        profile.work_experience = data['work_experience']
        profile.skills_technologies = data['skills_technologies']

        profile.save()

        return Response(200)
