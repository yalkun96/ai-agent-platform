from enum import Enum


class AIProvider(str, Enum):
    OpenAI = "openai"
    Anthropic = "anthropic"
    Google = "google"
