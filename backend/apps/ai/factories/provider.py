from apps.ai.exceptions import AIProviderConfigurationError
from apps.ai.interfaces.provider import AIProvider
from django.conf import settings

from apps.ai.providers.fake import FakeAIProvider
from apps.ai.providers.openAI import OpenAIProvider
from django.conf import settings
class AIProviderFactory:

    @staticmethod
    def create() -> AIProvider:
        provider = settings.AI_PROVIDER.lower()
        if provider == "fake":
            return FakeAIProvider()
        elif provider=="openai":
            return OpenAIProvider(
                api_key=settings.OPENAI_API_KEY,
                model=settings.OPENAI_MODEL
            )
        raise AIProviderConfigurationError(
            f"Unsupported AI provider: {provider}"
        )