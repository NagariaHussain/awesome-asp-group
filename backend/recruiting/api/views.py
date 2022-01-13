from rest_framework.decorators import api_view
from rest_framework.response import Response

from recruiting.models import JobPosting
from .serializers import JobPostingSerializer


@api_view(["GET"])
def get_all_job_postings(request):
    postings = JobPosting.objects.all()
    serializer = JobPostingSerializer(postings, many=True)
    return Response(serializer.data)
