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
    class InterviewRoundStatus(models.TextChoices):
        """Options for Interview Round Status"""

        NOT_STARTED = "not_started", "Not Started"
        IN_PROGRESS = "in_progress", "In Progress"
        COMPLETED = "completed", "Completed"

    created_at = models.DateTimeField(auto_now_add=True)
    interview = models.ForeignKey(
        Interview, on_delete=models.CASCADE, related_name="rounds"
    )
    index = models.IntegerField(default=0)
    status = models.CharField(
        max_length=25,
        choices=InterviewRoundStatus.choices,
        default=InterviewRoundStatus.NOT_STARTED,
    )
    name = models.CharField(max_length=100, default="")

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = f"Round {self.index + 1}"

        super(InterviewRound, self).save(*args, **kwargs)

    def start(self):
        if self.status != self.InterviewRoundStatus.NOT_STARTED:
            return

        InterviewEvent.objects.create(
            interview_round=self,
            type=InterviewEvent.InterviewEventType.STARTED,
        )

        self.status = self.InterviewRoundStatus.IN_PROGRESS
        self.save()


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
        InterviewRound, on_delete=models.CASCADE, null=True, related_name="events"
    )


class Communication(models.Model):
    body = models.TextField()
    sender = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    event = models.OneToOneField(InterviewEvent, on_delete=models.CASCADE, null=True)


class InterviewFileAttachment(models.Model):
    uploader = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    file = models.FileField()
    event = models.OneToOneField(
        InterviewEvent, on_delete=models.CASCADE, related_name="attachment"
    )


class InterviewRoundAssignment(models.Model):
    interview_round = models.ForeignKey(
        InterviewRound, on_delete=models.CASCADE, related_name="assignments"
    )
    assignee = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="assignments"
    )


class InterviewRoundAssignmentEvent(models.Model):
    event = models.OneToOneField(
        InterviewEvent, on_delete=models.CASCADE, related_name="assignment_event"
    )
    assignment = models.OneToOneField(
        InterviewRoundAssignment, on_delete=models.CASCADE, related_name="assignment"
    )

    def create_assignment(self, interview_round, assignee):
        assignment = InterviewRoundAssignment(
            interview_round=interview_round, assignee=assignee
        )
        assignment.save()
        self.assignment = assignment
        self.save()
