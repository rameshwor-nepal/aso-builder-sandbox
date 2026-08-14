from apps.ai.exceptions import AIProviderConfigurationError
from apps.ai.interfaces.provider import AIProvider
from django.conf import settings

from apps.ai.providers.fake import FakeAIProvider

class AIProviderFactory:

    @staticmethod
    def create() -> AIProvider:
        provider = settings.AI_PROVIDER.lower()
        if provider == "fake":
            return FakeAIProvider()
        raise AIProviderConfigurationError(
            f"Unsupported AI provider: {provider}"
        )