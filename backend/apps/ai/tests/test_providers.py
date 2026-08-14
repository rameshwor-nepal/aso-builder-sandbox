from apps.ai.providers.fake import FakeAIProvider
from apps.ai.schemas import AIAnalysisRequest, AIAnalysisResult
from apps.ai.exceptions import AIProviderError, AIProviderNetworkError, AIProviderTimeOutError, AIProviderUnavailableError

def test_fake_provider_returns_analysis_result():
    request = AIAnalysisRequest(
        title="Improve hospital appointment scheduling",
        description="Patients experience long waiting times..."
    )
    provider = FakeAIProvider()
    result = provider.analyze(request)
    assert isinstance(result, AIAnalysisResult)
    assert result.summary==("Analysis generated for: Improve hospital appointment scheduling")
    
def test_ai_provider_error_inherit_from_exception():
    assert issubclass(AIProviderError, Exception)

def test_network_error_inherit_from_ai_provider_error():
    assert issubclass(AIProviderNetworkError, AIProviderError)

def test_timeout_error_inherit_from_ai_provider_error():
    assert issubclass(AIProviderTimeOutError, AIProviderError)

def test_unavailable_error_inherit_from_ai_provider_error():
    assert issubclass(AIProviderUnavailableError, AIProviderError)
    
