from rest_framework.decorators import api_view
from rest_framework.response import Response

from recruiting.models import JobPosting
from .serializers import JobPostingSerializer


@api_view(["GET"])
def get_all_job_postings(request):
    postings = JobPosting.objects.all()
    serializer = JobPostingSerializer(postings, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def publish_job_posting(request, id):
    job_posting = JobPosting.objects.get(id=id)
    job_posting.is_published = True
    job_posting.save()
    return Response(True)
