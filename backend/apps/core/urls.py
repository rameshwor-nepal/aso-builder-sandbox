from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('index/', views.Index, name='index'),
    path('health/', HealthCheckAPIView.as_view(), name='health')
]