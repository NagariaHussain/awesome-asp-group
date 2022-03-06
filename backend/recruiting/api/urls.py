from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_all_job_postings),
    path("job-postings", views.get_all_job_postings),
    path("job-published-postings", views.get_all_published_postings),
    path("job-postings/new", views.create_job_posting),
    path("job-postings/<int:id>", views.get_job_posting_details),
    path("job-postings/<int:id>/publish", views.publish_job_posting),
    path("job-postings/<int:id>/unlist", views.unlist_job_posting),

    #########################
    # Job Applications routes
    #########################
    path("job-applications", views.get_all_job_applications),

    ##################
    # Interview routes
    ##################
    path("upload-interview-attachment", views.upload_interview_attachment),

    #############
    # Auth routes
    #############
    path("login", views.login_user),
    path("signup", views.signup_user),
    path("logout", views.logout_user),
    path("account", views.get_account_info),
]
