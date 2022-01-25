import logging

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserProfileSerializer
from .models import UserProfile

logger = logging.getLogger(__name__)


@api_view(["GET"])
def get_profile(request, id):
    """
    Get user profile by id (segment)
    """
    try:
        profile = UserProfile.objects.get(pk=id)
    except UserProfile.DoesNotExist:
        return Response(404)

    serializer = UserProfileSerializer(profile)
    return Response(serializer.data, 200)


@api_view(["POST"])
def save_profile(request):
    """
    Save user profile
    """
    logger.info(f"Payload of the request={request.data}")
    serializer = UserProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(201)
    return Response(serializer.errors, 400)
