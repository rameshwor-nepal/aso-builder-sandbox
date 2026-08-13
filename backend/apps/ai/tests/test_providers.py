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