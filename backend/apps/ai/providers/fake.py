from apps.ai.interfaces.provider import AIProvider
from apps.ai.schemas import AIAnalysisRequest, AIAnalysisResult


class FakeAIProvider(AIProvider):
    def analyze(self, request: AIAnalysisRequest,) -> AIAnalysisResult:
        return AIAnalysisResult(
            summary=f"Analysis generated for: {request.title}"
        )