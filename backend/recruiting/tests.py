from django.test import TestCase

from recruiting.models import JobPosting, JobApplication
from recruiting.models.interview import (
    Interview,
    InterviewEvent,
    InterviewRound,
    Communication,
)
from django.contrib.auth.models import User


class InterviewTestCase(TestCase):
    def setUp(self) -> None:
        self.test_user = User.objects.create_user(
            username="test_user",
            password="test_password",
        )

        self.test_job_posting = JobPosting.objects.create(
            job_title="test_job_title",
            description="test_description",
            company=self.test_user,
        )

        self.test_job_application = JobApplication.objects.create(
            job_posting=self.test_job_posting,
            applicant=self.test_user,
        )

        self.test_interview = Interview.objects.create(
            application=self.test_job_application
        )

        self.test_interview_rounds = {}
        for i in range(1, 4):
            self.test_interview_rounds[i] = InterviewRound.objects.create(
                interview=self.test_interview, index=i
            )

    def test_get_interview_rounds(self):
        # Get the rounds for the test interview
        rounds = InterviewRound.objects.filter(interview=self.test_interview).order_by(
            "index"
        )

        # There are 3 rounds
        self.assertEqual(len(rounds), 3)

        # Order should be same
        self.assertEqual(rounds[0], self.test_interview_rounds[1])
        self.assertEqual(rounds[1], self.test_interview_rounds[2])
        self.assertEqual(rounds[2], self.test_interview_rounds[3])
