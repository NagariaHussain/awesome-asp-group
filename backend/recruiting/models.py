from django.db import models

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
