from apps.ai.interfaces.provider import AIProvider


class OpenAIProvider(AIProvider):
    def __init__(self, api_key:str, model:str):
        self.api_key=api_key
        self.model=model