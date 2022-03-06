from django.db import models
from django.contrib.auth.models import User

# import Models related to interview process
from .interview import (
    Interview,
    Communication,
    InterviewEvent,
    InterviewRound,
    InterviewFileAttachment,
)


class Profile(models.Model):
    """To store additional user info like `user_type`"""

    class UserType(models.TextChoices):
        COMPANY = "C", "Company"
        INDIVIDUAL = "I", "Individual"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(
        max_length=1, choices=UserType.choices, default=UserType.COMPANY
    )
    avatar_image = models.FileField(upload_to="avatars/", blank=True)

    def __str__(self):
        return f"{self.user_type}:{self.user.username}"


class JobPosting(models.Model):
    job_title = models.CharField(max_length=255, null=False)
    description = models.TextField(default="")
    is_published = models.BooleanField(default=False)
    location = models.CharField(max_length=255, null=False)
    company = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="job_postings"
    )
    department = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.job_title} : {self.location}"

    @property
    def company_name(self):
        return self.company.fullname


class JobApplication(models.Model):
    class Status(models.TextChoices):
        # Status of job application
        OPEN = "Open", "Open"
        WAITING_FOR_MATERIALS = "Waiting for materials", "Waiting for materials"
        IN_INTERVIEW = "In Interview", "In Interview"
        ACCEPTED = "Accepted", "Accepted"
        REJECTED = "Rejected", "Rejected"

    # An application is linked to a job posting
    # (JobPosting) and an applicant (User)
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE, null=False)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    resume_link = models.URLField(
        ("Link to applicant's resume!"),
        max_length=255,
        unique=True,
        blank=True,
    )

    status = models.CharField(
        max_length=255, choices=Status.choices, default=Status.OPEN
    )
    expected_salary = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"""
        JobApplication = [
            applicant = {self.applicant.username},
            job_posting = {self.job_posting.job_title},
        ]
        """
