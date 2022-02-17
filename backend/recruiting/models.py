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


# Create your models here.
class JobPosting(models.Model):
    job_title = models.CharField(max_length=255)
    description = models.TextField()
    is_published = models.BooleanField(default=False)
    location = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.job_title} : {self.location}"
