import pytest
from apps.ai.providers.fake import FakeAIProvider
from apps.ai.schemas import AIAnalysisRequest
from apps.ai.services.analysis import AIAnalysisService
from apps.intake.models import BusinessProblem

@pytest.mark.django_db  
def test_analyze_correct_ai_request():
    problem=BusinessProblem.objects.create(
                title="Technology Problems",
                description=( "Outdated systems, software failures, or lack of automation reduce efficiency and increase operating costs." )
            )
    provider = FakeAIProvider()
    service = AIAnalysisService(provider)
    service.analyze(problem)
    assert provider.request_received ==AIAnalysisRequest(
                title="Technology Problems",
                description=( "Outdated systems, software failures, or lack of automation reduce efficiency and increase operating costs." )
            )
    
@pytest.mark.django_db  
def test_analyze_correct_ai_service_response():
    problem=BusinessProblem.objects.create(
                title="Cash Flow Problems",
                description=( "The business struggles to maintain enough cash to cover expenses, salaries, suppliers, or other obligations." )
            )
    provider = FakeAIProvider()
    service = AIAnalysisService(provider)
    result = service.analyze(problem)
    assert result.summary==("Analysis generated for: Cash Flow Problems")
    
    
       