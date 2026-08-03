from django.urls import path
from .views import *

urlpatterns = [
    path('health/', HealthCheckAPIView.as_view(), name='health')
]