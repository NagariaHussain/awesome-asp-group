from django.db import models


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


class InterviewRound(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    index = models.IntegerField(default=0)


class InterviewEvent(models.Model):
    class InterviewEventType(models.TextChoices):
        """Options for event type"""

        STARTED = "started", "Started"
        INTERNAL_COMMENT = "internal_comment", "Internal Comment"
        FILE_ATTACHED = "file_attached", "File Attached"
        ASSIGNMENT = "assignment", "Assignment"

    type = models.CharField(choices=InterviewEventType.choices, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    interview_round = models.ForeignKey(
        InterviewRound, on_delete=models.CASCADE, null=True
    )


class Communication(models.Model):
    body = models.TextField()
    sender = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    event = models.OneToOneField(InterviewEvent, on_delete=models.CASCADE, null=True)


class InterviewFileAttachment(models.Model):
    file = models.FileField()
    event = models.OneToOneField(InterviewEvent, on_delete=models.CASCADE)
