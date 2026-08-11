import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from apps.intake.models import BusinessProblem, ProblemStatuses


# test get api 
@pytest.mark.django_db   
def test_list_returns_empty_when_no_problems_exist():
    client = APIClient()
    response = client.get(reverse("business_problem"))
    assert response.status_code == status.HTTP_200_OK
    assert response.data["data"]["count"] == 0

# test get api with data    
@pytest.mark.django_db
def test_list_returns_business_problems():
    BusinessProblem.objects.create(
        title="Manual Claim Review",
        description=(
            "Hospital staff manually verify insurance claims "
            "before approval."
        )
    )
    client = APIClient()
    response = client.get(reverse("business_problem"))
    assert response.status_code == status.HTTP_200_OK
    assert response.data["data"]["count"] == 1
    assert response.data["data"]["results"][0]["title"] == "Manual Claim Review"
     
# test create/post api with short title    
@pytest.mark.django_db   
def test_create_with_short_title_returns_400():
    payload = {"title": "short", "description": "x" * 60}
    client = APIClient()
    response = client.post(reverse("business_problem"), payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert BusinessProblem.objects.count() == 0
    
# test create/post api with attempt to change status   
@pytest.mark.django_db   
def test_create_ignores_client_supplied_status():
    payload = {"title": "Client attempts to set status directly", "description": "x" * 60, "status": ProblemStatuses.COMPLETED_AI}
    client = APIClient()
    response = client.post(reverse("business_problem"), payload)
    assert response.data["data"]["status"] == ProblemStatuses.PENDING_AI
 
 #test get business problem by id
@pytest.mark.django_db  
def test_retrieve_existing_problem_returns_200():
    problem=BusinessProblem.objects.create(
            title="Manual Claim Review",
            description=( "Hospital staff manually verify insurance claims before approval." )
        )
    client = APIClient()
    url = reverse("detail_business_problem", kwargs={"pk": problem.id})
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["data"]["id"] == problem.id  


@pytest.mark.django_db  
def test_retrieve_nonexistent_problem_returns_404():
    client = APIClient()
    url = reverse("detail_business_problem", kwargs={"pk": 99})
    response = client.get(url)
    assert response.status_code == status.HTTP_404_NOT_FOUND


# ---- UPDATE ---- PATCH
@pytest.mark.django_db  
def test_patch_updates_title_only():
    problem=BusinessProblem.objects.create(
                title="Manual Claim Review",
                description=( "Hospital staff manually verify insurance claims before approval." )
            )
    client = APIClient()
    url = reverse("detail_business_problem", kwargs={"pk": problem.pk})
    response = client.patch(url, {"title": "Updated title after patching this record"})
    assert response.status_code == status.HTTP_200_OK
    problem.refresh_from_db()
    assert problem.title == "Updated title after patching this record"
 
    
 #------ UPDATE ---- PUT
@pytest.mark.django_db  
def test_put_updates_():
    problem=BusinessProblem.objects.create(
                title="Manual Claim Review",
                description=( "Hospital staff manually verify insurance claims before approval." )
            )
    client = APIClient()
    url = reverse("detail_business_problem", kwargs={"pk": problem.pk})
    response = client.put(url, {"title": "Updated title after patching this record", "description":"Update after put method: Hospital staff manually verify insurance claims before approval. "})
    assert response.status_code == status.HTTP_200_OK
    problem.refresh_from_db()
    assert problem.title == "Updated title after patching this record"   

    
 #test delete api
@pytest.mark.django_db  
def test_delete_200():
    problem=BusinessProblem.objects.create(
            title="Manual Claim Review",
            description=( "Hospital staff manually verify insurance claims before approval." )
        )
    client = APIClient()
    url = reverse("detail_business_problem", kwargs={"pk": problem.id})
    response = client.delete(url)
    assert response.status_code == status.HTTP_200_OK
    assert not BusinessProblem.objects.filter(pk=problem.pk).exists()  
