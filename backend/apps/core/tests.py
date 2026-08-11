
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


def test_health_check():
    client = APIClient()

    response = client.get(reverse("health"))
    assert response.status_code == status.HTTP_200_OK
    assert response.data["status"] == "healthy"
    assert response.data["service"] == "aso-builder-sandbox"
    assert response.data["version"] == "0.1.0"
    assert "timestamp" in response.data
    