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

        self.test_interview_round_1 = InterviewRound.objects.create(
            interview=self.test_interview, index=1
        )

        self.test_interview_round_2 = InterviewRound.objects.create(
            interview=self.test_interview, index=2
        )

        self.test_interview_round_3 = InterviewRound.objects.create(
            interview=self.test_interview, index=3
        )

    def test_get_interview_rounds(self):
        rounds = InterviewRound.objects.filter(interview=self.test_interview)

        self.assertEqual(len(rounds), 3)
