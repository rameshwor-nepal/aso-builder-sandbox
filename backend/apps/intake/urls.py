from django.urls import path
from .views import BusinessProblemApiView, BusinessProblemDetailApiView

urlpatterns = [
    path("business-problem/", BusinessProblemApiView.as_view(), name='business_problem'),
    path("business-problem/<int:pk>/", BusinessProblemDetailApiView.as_view(), name="detail_business_problem")
]