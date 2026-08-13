import pytest

from apps.ai.exceptions import AIProviderConfigurationError
from apps.ai.factories.provider import AIProviderFactory
from apps.ai.interfaces.provider import AIProvider
from apps.ai.providers.fake import FakeAIProvider


def test_fake_provider_is_returned(settings):
    settings.AI_PROVIDER = "fake"
    provider = AIProviderFactory.create()
    assert isinstance(provider, FakeAIProvider)


def test_returned_provider_satisfies_ai_provider(settings):
    settings.AI_PROVIDER = "fake"
    provider = AIProviderFactory.create()
    assert isinstance(provider, AIProvider)


def test_unknown_provider_raises_configuration_error(settings):
    settings.AI_PROVIDER = "unknown"
    with pytest.raises(AIProviderConfigurationError):
        AIProviderFactory.create()