from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_all_job_postings),
    path("job-postings", views.get_all_job_postings),
    path("publish-jp/<int:id>", views.publish_job_posting),
    path("login", views.login_user),
    path("signup", views.signup_user),
    path("logout", views.logout_user),
    path("account", views.get_account_info),
]
