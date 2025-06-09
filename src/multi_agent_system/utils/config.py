"""Configuration utilities for the multi-agent system."""

import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Configuration class for the multi-agent system."""
    
    # Model configuration
    DEFAULT_MODEL: str = os.getenv("DEFAULT_MODEL", "gpt-3.5-turbo")
    DEFAULT_TEMPERATURE: float = float(os.getenv("DEFAULT_TEMPERATURE", "0.7"))
    DEFAULT_MAX_TOKENS: int = int(os.getenv("DEFAULT_MAX_TOKENS", "1000"))
    
    # Language configuration
    DEFAULT_LANGUAGE: str = os.getenv("DEFAULT_LANGUAGE", "ja")  # 日本語をデフォルトに設定
    
    # API Keys
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    
    # AWS Bedrock configuration
    AWS_ACCESS_KEY_ID: Optional[str] = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY: Optional[str] = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_DEFAULT_REGION: str = os.getenv("AWS_DEFAULT_REGION", "us-east-1")
    
    @classmethod
    def validate_config(cls) -> bool:
        """Validate that required configuration is present."""
        # For this demo, we'll use a simple mock implementation
        # In a real implementation, you would check for actual API keys
        return True
    
    @classmethod
    def get_model_config(cls) -> dict:
        """Get model configuration dictionary."""
        return {
            "model": cls.DEFAULT_MODEL,
            "temperature": cls.DEFAULT_TEMPERATURE,
            "max_tokens": cls.DEFAULT_MAX_TOKENS,
        }

