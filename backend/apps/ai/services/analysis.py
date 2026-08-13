from apps.ai.interfaces.provider import AIProvider
from apps.ai.schemas import AIAnalysisRequest, AIAnalysisResult


class AIAnalysisService:
    def __init__(self, provider:AIProvider):
        self.provider = provider
        
    def analyze(self, problem) ->AIAnalysisResult:
        request = AIAnalysisRequest(
            title=problem.title,
            description=problem.description
        )
        return self.provider.analyze(request)
        