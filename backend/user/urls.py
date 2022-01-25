from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r"^api/v1/users/(?P<id>[0-9]+)$", views.get_profile, name="get_profile"),
    re_path(r"^api/v1/users", views.save_profile, name="save_profile"),
]
