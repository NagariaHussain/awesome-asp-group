from django.db import models
from enum import Enum

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


class ApplicationState(Enum):
    PENDING = "PENDING"
    PROCESSED = "PROCESSED"
    BOCKED = "BLOCKED"
    
class JobApplication(models.Model):
    job_posting = models.URLField(
        ("Link to job posting!"), 
        max_length=255, 
        db_index=True, 
        unique=True, 
        blank=True
    )
    resume_link = models.URLField(
        ("Link to applicant's resume!"),
        max_length=255, 
        db_index=True, 
        unique=True, 
        blank=True
    ) 
    applicant_name = models.CharField(max_length=255)
    applicant_age = models.IntegerField()
    applicant_email = models.CharField(max_length=255)
    phone_screening = models.BooleanField(default=False)
    application_state = models.CharField(max_length=255, default=ApplicationState.PENDING)
    expected_salary = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"""
        JobApplication = [
            applicant_name = {self.applicant_name},
            applicant_email = {self.applicant_email},
            created_at = {self.created_at},
            phone_screening = {self.phone_screening},
        ]
        """