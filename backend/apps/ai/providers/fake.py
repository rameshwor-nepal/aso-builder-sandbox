from apps.ai.interfaces.provider import AIProvider
from apps.ai.schemas import AIAnalysisRequest, AIAnalysisResult


class FakeAIProvider(AIProvider):
    def __init__(self, error=None):
        self.request_received=None
        self.error=error
        
    def analyze(self, request: AIAnalysisRequest,) -> AIAnalysisResult:
        self.request_received=request
        if self.error:
            raise self.error
        return AIAnalysisResult(
            summary=f"Analysis generated for: {request.title}"
        )