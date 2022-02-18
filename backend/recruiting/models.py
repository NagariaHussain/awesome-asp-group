from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """To store additional user info like `user_type`"""

    class UserType(models.TextChoices):
        COMPANY = "C", "Company"
        INDIVIDUAL = "I", "Individual"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(
        max_length=1, choices=UserType.choices, default=UserType.COMPANY
    )

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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.job_title} : {self.location}"
