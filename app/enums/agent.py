from enum import Enum

class AIModel(str, Enum):
    GPT_5 = "gpt-5"
    CLAUDE =  "claude"
    GEMINI = "gemini"