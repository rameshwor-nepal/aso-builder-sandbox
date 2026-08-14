from abc import ABC, abstractmethod

from apps.ai.schemas import AIAnalysisRequest, AIAnalysisResult


class AIProvider(ABC):

    @abstractmethod
    def analyze( self, request: AIAnalysisRequest,) -> AIAnalysisResult:
        pass