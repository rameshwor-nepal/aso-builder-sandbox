import openai
from apps.ai.exceptions import AIProviderNetworkError, AIProviderRateLimitError, AIProviderTimeOutError, AIProviderUnavailableError
from apps.ai.interfaces.provider import AIProvider
from apps.ai.schemas import AIAnalysisRequest, AIAnalysisResult

class OpenAIProvider(AIProvider):
    def __init__(self, client,model:str):
        self.client=client
        self.model=model
        
    def analyze(self, request: AIAnalysisRequest,) -> AIAnalysisResult:
        try:
            response = self.client.responses.create(
                model=self.model,
                instructions="Analyze the business problem and provide a concise summary.",
                input=(
                    f"Title: {request.title}\n\n"
                    f"Description: {request.description}"
                ),
            )
            return AIAnalysisResult(
                summary=response.output_text
            )
        except openai.APITimeoutError as exec:
                raise AIProviderTimeOutError("AI provider request timed out.") from exec
        except openai.APIConnectionError as exec:
                raise AIProviderNetworkError("Unable to connect to AI provider.") from exec
        except openai.RateLimitError as exec:
                raise AIProviderRateLimitError( "AI provider rate limit exceeded.") from exec
        except openai.InternalServerError as exec:
                raise AIProviderUnavailableError("AI provider is currently unavailable.") from exec