from django.db import models


# DO THE UI FIRST!
# DON"T WORRY ABOUT THE BACKEND!

class Interview(models.Model):
    class InterviewStatus(models.TextChoices):
        """Options for Interview Status"""

        NOT_STARTED = "not_started", "Not Started"
        IN_PROGRESS = "in_progress", "In Progress"
        COMPLETED = "completed", "Completed"

    application = models.ForeignKey(
        "recruiting.JobApplication", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=25,
        choices=InterviewStatus.choices,
        default=InterviewStatus.NOT_STARTED,
    )


class Communication(models.Model):
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey("auth.User", on_delete=models.CASCADE)

