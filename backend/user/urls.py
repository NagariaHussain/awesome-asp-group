from django.urls import re_path, path
from . import views

urlpatterns = [
    re_path(r"^api/v1/users/(?P<username>[a-zA-Z]+)$", views.get_profile, name="get_profile"),
    re_path(r"^api/v1/users", views.save_profile, name="save_profile"),
    path("api/v1/apply", views.apply_job, name="apply_job"),
    path("api/v1/applied/<str:username>", views.applied_job, name="applied_job")
]
