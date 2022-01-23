from django.urls import reverse
from rest_framework.test import APITestCase, APIClient

from ..serializers import UserProfileSerializer


class UserProfileTestCase(APITestCase):
    """
    Test cases for User Profile functionality.
    """

    @classmethod
    def profile_fixture(cls):
        return {
            "full_name": "David Manukian",
            "title": "Senior Data Engineer",
            "location": "Gyumri, Armenia",
            "desired_location": "Good place",
            "desired_salary": 7000,
            "about": "person",
            "work_experience": {
                "EPAM": {"title": "Software Engineer"},
                "Self-Employed": {"title": "Software Engineer"},
                "Plarium": {"title": "Data Engineer"},
            },
            "skills_technologies": {
                "Java": "Advanced",
                "Scala": "Upper-Intermediate",
                "Python": "Intermediate",
            },
            "education": {
                "University": "Goldsmiths, University of London",
                "Degree": "Bachelor Degree",
            },
            "license_certification": {"Provider": "Coursera"},
            "languages": {
                "Russian": "Native",
                "Armenia": "Native",
                "English": "Advanced",
            },
        }

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.client = APIClient()

        serializer = UserProfileSerializer(data=cls.profile_fixture())
        if serializer.is_valid():
            cls.user_profile = serializer.save()

    def test_get_profile(self):
        response = self.client.get(
            reverse("get_profile", kwargs={"id": self.user_profile.id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["full_name"], self.user_profile.full_name)
        self.assertEqual(response.data["title"], self.user_profile.title)

    def test_save_profile(self):
        response = self.client.post(reverse("save_profile"), self.profile_fixture())
        self.assertEqual(response.status_code, 200)
