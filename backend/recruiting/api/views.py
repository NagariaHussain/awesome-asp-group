import json
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from django.contrib.auth.models import User
from recruiting.models import JobPosting, Profile
from django.contrib.auth.decorators import login_required
from .serializers import JobPostingSerializer, UserSerializer
from django.contrib.auth import authenticate, login, get_user, logout


@api_view(["GET"])
@login_required
def get_all_job_postings(request):
    postings = request.user.job_postings.all().order_by("-created_at")
    serializer = JobPostingSerializer(postings, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_job_posting(request):
    # postings = request.user.job_postings.add
    serializer = JobPostingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(company=request.user)
        return Response(serializer.data)
    else:
        return Response(serializer.errors, exception=True, status=400)


@api_view(["GET"])
def publish_job_posting(request, id):
    job_posting = JobPosting.objects.get(id=id)
    job_posting.is_published = True
    job_posting.save()
    return Response(True)


@api_view(["POST"])
def signup_user(request):
    data = json.loads(request.body)
    user = UserSerializer(data=data)

    if user.is_valid():
        new_user = User.objects.create_user(
            username=data["username"],
            password=data["password"],
            first_name=data["firstName"],
            last_name=data["lastName"],
        )
        new_user.save()

        # Create profile with user_type set to data["userType"]
        Profile.objects.create(user=new_user, user_type=data["profile"]["user_type"])

        login(request, new_user)
        return Response(user.data)
    else:
        return Response(user.errors, status=400, exception=True)


@api_view(["GET"])
def logout_user(request):
    logout(request)
    return Response(True)


@api_view(["POST"])
def login_user(request):
    received_json_data = request.data
    username = received_json_data["username"]
    password = received_json_data["password"]

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    else:
        # Return an 'invalid login' error message.
        # Username and password does not match
        return Response(
            "Username and password does not match", status=403, exception=True
        )


@api_view(["GET"])
def get_account_info(request):
    if not request.user.is_authenticated:
        return Response("User not authenticated", status=403, exception=True)
    else:
        serializer = UserSerializer(get_user(request))
        return Response(serializer.data)
