from apps.ai.exceptions import AIProviderConfigurationError
from apps.ai.interfaces.provider import AIProvider
from apps.ai.providers.fake import FakeAIProvider
from apps.ai.providers.openAI import OpenAIProvider
from django.conf import settings
from openai import OpenAI

class AIProviderFactory:

    @staticmethod
    def create() -> AIProvider:
        provider = settings.AI_PROVIDER.lower()
        if provider == "fake":
            return FakeAIProvider()
        if provider=="openai":
            if not settings.OPENAI_API_KEY:
                raise AIProviderConfigurationError("OPENAI_API_KEY is required when AI_PROVIDER is 'openai'.")
            if not settings.OPENAI_MODEL:
                raise AIProviderConfigurationError("OPENAI_MODEL is required when AI_PROVIDER is 'openai'.")
            
            client=OpenAI(api_key=settings.OPENAI_API_KEY)
            return OpenAIProvider(
                client=client,
                model=settings.OPENAI_MODEL
            )
        raise AIProviderConfigurationError(
            f"Unsupported AI provider: {provider}"
        )