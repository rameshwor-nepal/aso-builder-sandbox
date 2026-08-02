from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import now
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

def Index(request):
    return HttpResponse("Healthy!!")


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
                "service": "my-api",
                "timestamp": now().isoformat(),
                "version": "1.0.0",
            },
            status=status.HTTP_200_OK,
        )