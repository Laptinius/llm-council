"""Configuration for the LLM Council."""

import os
from dotenv import load_dotenv

load_dotenv()

# OpenRouter API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Council members - list of OpenRouter model identifiers
COUNCIL_MODELS = [
    # "openai/gpt-5.1",
    # "google/gemini-3-pro-preview",
    # "anthropic/claude-sonnet-4.5",
    # "x-ai/grok-4",

    "kwaipilot/kat-coder-pro:free",
    "mistralai/mistral-small-3.1-24b-instruct:free",
    "alibaba/tongyi-deepresearch-30b-a3b:free",
    "nousresearch/hermes-3-llama-3.1-405b:free",
]

# Chairman model - synthesizes final response
CHAIRMAN_MODEL = "nousresearch/hermes-3-llama-3.1-405b:free"

# OpenRouter API endpoint
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Data directory for conversation storage
DATA_DIR = "data/conversations"
