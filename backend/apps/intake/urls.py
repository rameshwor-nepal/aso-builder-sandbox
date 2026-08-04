from django.urls import path
from .views import *

urlpatterns = [
    path("business-problem/", BusinessProblemApiView.as_view(), name='business_problem')
]