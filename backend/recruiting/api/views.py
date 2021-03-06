import json
import time
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from recruiting.models import JobPosting, JobApplication, Profile
from recruiting.models.interview import (
    InterviewEvent,
    InterviewFileAttachment,
    Interview,
    InterviewRound,
    Communication,
    InterviewRoundAssignment,
    InterviewRoundAssignmentEvent,
)
from .serializers import (
    JobPostingSerializer,
    UserSerializer,
    ApplicationSerializer,
    CommentSerializer,
    InterviewRoundSerializer,
    InterviewEventSerializer,
    InterviewFileAttachmentSerializer,
    CommunicationSerializer,
)

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, get_user, logout


@api_view(["POST"])
def upload_interview_attachment(request, interview_round_id):
    file = request.FILES.get("uploaded_file")
    if not file:
        return Response("No file uploaded", status=400)
    else:
        interview_round = InterviewRound.objects.get(id=interview_round_id)
        interview_event = InterviewEvent.objects.create(
            type="file_attached", interview_round=interview_round
        )
        InterviewFileAttachment.objects.create(
            file=file, event=interview_event, uploader=request.user
        )
        return Response({"message": "File uploaded successfully"})


@api_view(["POST"])
def post_interview_comment(request):
    comment = CommentSerializer(data=request.data)
    if not comment.is_valid():
        return Response(comment.errors, status=400)
    else:
        time.sleep(1)  # To test loading
        interview_round = InterviewRound.objects.get(id=1)
        interview_event = InterviewEvent.objects.create(
            type="internal_comment", interview_round=interview_round
        )
        Communication.objects.create(
            body=comment.data["comment"], sender=request.user, event=interview_event
        )
        return Response({"message": "Comment posted successfully"})


@api_view(["POST"])
def create_interview_round_assignment(request):
    # TODO: get round and assignee (username) from request body
    interview_round = InterviewRound.objects.get(id=1)
    event = InterviewEvent.objects.create(
        type="assignment", interview_round=interview_round
    )
    assignee = request.user
    interview_round_assignment_event = InterviewRoundAssignmentEvent(event=event)
    interview_round_assignment_event.create_assignment(interview_round, assignee)
    return Response({"message": "Interview round assigned successfully"})


@api_view(["GET"])
def get_interview_round_details(request, interview_round_id):
    interview_round = InterviewRound.objects.get(id=interview_round_id)
    interview_event = InterviewEvent.objects.filter(
        interview_round=interview_round
    ).order_by("created_at")

    data = {
        "interview_round": InterviewRoundSerializer(interview_round).data,
        "interview_events": InterviewEventSerializer(interview_event, many=True).data,
    }

    return Response(data)


@api_view(["GET"])
@login_required
def get_all_job_postings(request):
    postings = request.user.job_postings.all().order_by("-created_at")
    serializer = JobPostingSerializer(postings, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@login_required
def get_all_published_postings(request):
    title = request.GET.get("title", "")
    postings = (
        JobPosting.objects.prefetch_related("company")
        .filter(is_published=True, job_title__icontains=title)
        .order_by("-created_at")
    )

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


@api_view(["GET"])
def unlist_job_posting(request, id):
    job_posting = JobPosting.objects.get(id=id)
    job_posting.is_published = False
    job_posting.save()
    return Response(True)


@api_view(["GET"])
def get_job_posting_details(request, id):
    job_posting = JobPosting.objects.get(id=id)
    serializer = JobPostingSerializer(job_posting)
    return Response(serializer.data)


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


@api_view(["GET"])
def get_all_job_applications(request):
    applications = JobApplication.objects.all()
    serializer = ApplicationSerializer(applications, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_application(request):
    data = json.loads(request.body)
    application = ApplicationSerializer(data=data)
    if application.is_valid():
        application.save()
        return Response(application.data)
    else:
        return Response(application.errors)
