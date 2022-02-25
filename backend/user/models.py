from django.db import models


# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    desired_location = models.CharField(max_length=255)
    gender = models.CharField(max_length=50)
    desired_salary = models.IntegerField()
    age = models.IntegerField()
    about = models.TextField()
    work_experience = models.JSONField()
    skills_technologies = models.JSONField()
    education = models.JSONField(blank=True)
    license_certification = models.JSONField(blank=True)
    languages = models.JSONField(blank=True)

    def __str__(self):
        return f"""
        UserProfile=[
            username={self.username},
            title={self.title},
            location={self.location},
            desired_location={self.desired_location},
            desired_salary={self.desired_salary},
            about={self.about},
            work_experience={self.work_experience},
            skills_technologies={self.skills_technologies},
            education={self.education},
            license_certification={self.license_certification},
            languages={self.languages}
        ]
        """
