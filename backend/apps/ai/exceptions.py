class AIProviderError(Exception):
    pass


class AIProviderNetworkError(AIProviderError):
    pass

class AIProviderTimeOutError(AIProviderError):
    pass

class AIProviderUnavailableError(AIProviderError):
    pass


class AIProviderConfigurationError(Exception):
    pass

class AIProviderRateLimitError(AIProviderError):
    pass