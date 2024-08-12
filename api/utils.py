from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings


@api_view(["GET"])
def health_check(request):
    return Response({"status ": "ok", "server_time": timezone.localtime(), "server_name": settings.SERVER_NAME})
