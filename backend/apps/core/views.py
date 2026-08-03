from django.http import HttpResponse
from django.utils.timezone import now
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class HealthCheckAPIView(APIView):
    """
    Health check endpoint.
    Used by monitoring systems to verify that the application
    is running and able to serve requests.
    """

    authentication_classes = []
    permission_classes = []

    def get(self, request):
        return Response(
            {
                "status": "healthy",
                "service": "aso-builder-sandbox",
                "timestamp": now().isoformat(),
                "version": "0.1.0",
            },
            status=status.HTTP_200_OK,
        )