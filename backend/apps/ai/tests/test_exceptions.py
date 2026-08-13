import pytest
from apps.ai.exceptions import AIProviderNetworkError, AIProviderTimeOutError, AIProviderUnavailableError
from apps.ai.providers.fake import FakeAIProvider
from apps.ai.schemas import AIAnalysisRequest, AIAnalysisResult


def test_fake_provider_returns_analysis_result():
    request = AIAnalysisRequest(
        title="Improve hospital appointment scheduling",
        description="Patients experience long waiting times..."
    )
    provider = FakeAIProvider()
    result = provider.analyze(request)
    assert isinstance(result, AIAnalysisResult)
    assert result.summary==("Analysis generated for: Improve hospital appointment scheduling")


def test_fake_network_error():
    provider=FakeAIProvider(error=AIProviderNetworkError())
    request = AIAnalysisRequest(
            title="Improve hospital appointment scheduling",
            description="Patients experience long waiting times..."
        )
    with pytest.raises(AIProviderNetworkError):
        provider.analyze(request)

def test_fake_timeout_error():
    provider=FakeAIProvider(error=AIProviderTimeOutError())
    request=AIAnalysisRequest(
        title="Improve hospital appointment scheduling",
        description="Patients experience long waiting times..."
    )
    with pytest.raises(AIProviderTimeOutError):
            provider.analyze(request)
            
def test_fake_unavailable_error():
    provider=FakeAIProvider(error=AIProviderUnavailableError())
    request=AIAnalysisRequest(
        title="Improve hospital appointment scheduling",
        description="Patients experience long waiting times..."
    )
    with pytest.raises(AIProviderUnavailableError):
            provider.analyze(request)
            
