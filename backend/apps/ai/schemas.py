from dataclasses import dataclass


@dataclass(frozen=True)
class AIAnalysisRequest:
    title: str
    description: str

@dataclass(frozen=True)
class AIAnalysisResult:
    summary: str