from unittest.mock import Mock, patch
import openai
import pytest
from apps.ai.exceptions import AIProviderConfigurationError, AIProviderNetworkError, AIProviderRateLimitError, AIProviderTimeOutError, AIProviderUnavailableError
from apps.ai.factories.provider import AIProviderFactory
from apps.ai.providers.openAI import OpenAIProvider
from apps.ai.schemas import AIAnalysisRequest, AIAnalysisResult

def test_openai_provider_requires_api_key(settings):
    settings.AI_PROVIDER = "openai"
    settings.OPENAI_API_KEY = ""
    settings.OPENAI_MODEL = "test-model"

    with pytest.raises( AIProviderConfigurationError, match="OPENAI_API_KEY is required"):
        AIProviderFactory.create()

def test_openai_provider_requires_model(settings):
    settings.AI_PROVIDER = "openai"
    settings.OPENAI_API_KEY = "test-api-key"
    settings.OPENAI_MODEL = ""

    with pytest.raises( AIProviderConfigurationError, match="OPENAI_MODEL is required"):
        AIProviderFactory.create()
           
def test_openai_provider_is_returned(settings):
    settings.AI_PROVIDER = "openai"
    settings.OPENAI_API_KEY = "test-api-key"
    settings.OPENAI_MODEL = "test-model"

    provider = AIProviderFactory.create()

    assert isinstance(provider, OpenAIProvider)
    # assert provider.api_key == "test-api-key"
    assert provider.model == "test-model"
    
def test_openai_provider_sends_correst_request():
    client = Mock()
    response = Mock()
    response.output_text="This is generated analysis"
    client.responses.create.return_value=response
    
    provider = OpenAIProvider(
        client=client,
        model="test-model"
    )
    request = AIAnalysisRequest(
        title="Low Productivity",
        description="Employees or processes are not operating efficiently, leading to delays, wasted resources, and lower output."
    )
    result = provider.analyze(request=request)
    client.responses.create.assert_called_once_with(
        model="test-model",
        instructions="Analyze the business problem and provide a concise summary.",
        input=(
            "Title: Low Productivity\n\n"
            "Description: Employees or processes are not operating efficiently, leading to delays, wasted resources, and lower output."
        ),
    )
    assert isinstance(result, AIAnalysisResult)
    assert result.summary == "This is generated analysis"

@pytest.fixture
def client():
    return Mock()


@pytest.fixture
def provider(client):
    return OpenAIProvider(
        client=client,
        model="test-model",
    )


@pytest.fixture
def api_request():
    return AIAnalysisRequest(
        title="Low Productivity",
        description=(
            "Employees or processes are not operating efficiently, "
            "leading to delays, wasted resources, and lower output."
        ),
    )
    
def test_openai_network_error(client, provider, api_request):
    client.responses.create.side_effect=openai.APIConnectionError(request=Mock())
    with pytest.raises(AIProviderNetworkError):
        provider.analyze(api_request)
        
        
def test_openai_timeout_error(client, provider, api_request):
    client.responses.create.side_effect=openai.APITimeoutError(request=Mock())
    with pytest.raises(AIProviderTimeOutError):
        provider.analyze(api_request)
        
        
def test_openai_internal_server_error(client, provider, api_request):
    client.responses.create.side_effect=openai.InternalServerError("OpenAI server error",
        response=Mock(),
        body=None,
    )
    with pytest.raises(AIProviderUnavailableError):
        provider.analyze(api_request)
        
        
def test_openai_ratelimit_error(client, provider, api_request):
    client.responses.create.side_effect=openai.RateLimitError("Rate limit exceeded",
        response=Mock(),
        body=None,)
    with pytest.raises(AIProviderRateLimitError):
        provider.analyze(api_request)
        

def test_unexpected_error_is_not_swallowed(client, provider, api_request):
    client.responses.create.side_effect = ValueError("unexpected")

    with pytest.raises(ValueError, match="unexpected"):
        provider.analyze(api_request)


def test_factory_creates_openai_provider(settings):
    settings.AI_PROVIDER = "openai"
    settings.OPENAI_API_KEY = "test-api-key"
    settings.OPENAI_MODEL = "test-model"
    mock_client = Mock()
    
    with patch( "apps.ai.factories.provider.OpenAI", return_value=mock_client,) as mock_openai:
        provider = AIProviderFactory.create()
    mock_openai.assert_called_once_with( api_key="test-api-key" )

    assert isinstance(provider, OpenAIProvider)
    assert provider.client is mock_client
    assert provider.model == "test-model"