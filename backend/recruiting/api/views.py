import json
from rest_framework.decorators import api_view
from rest_framework.response import Response

from recruiting.models import JobPosting
from .serializers import JobPostingSerializer, UserSerializer
from django.contrib.auth import authenticate, login, get_user, logout


@api_view(["GET"])
def get_all_job_postings(request):
    postings = JobPosting.objects.all()
    serializer = JobPostingSerializer(postings, many=True)
    return Response(serializer.data)


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
        user.save()
        return Response(user.data)
    else:
        return Response(user.errors)


@api_view(["GET"])
def logout_user(request):
    logout(request)
    return Response(True)


@api_view(["POST"])
def login_user(request):
    received_json_data = json.loads(request.body)
    username = received_json_data["username"]
    password = received_json_data["password"]

    print(received_json_data)

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
