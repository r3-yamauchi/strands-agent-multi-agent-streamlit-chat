"""Base agent class for the multi-agent system."""

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional
from strands import Agent
from strands.models.openai import OpenAIModel
from ..utils.config import Config


class BaseAgent(ABC):
    """Base class for all agents in the multi-agent system."""
    
    def __init__(self, name: str, system_prompt: str, **kwargs):
        """Initialize the base agent.
        
        Args:
            name: The name of the agent
            system_prompt: The system prompt for the agent
            **kwargs: Additional configuration parameters
        """
        self.name = name
        self.system_prompt = system_prompt
        self.config = kwargs
        self.language = kwargs.get('language', Config.DEFAULT_LANGUAGE)
        
        # 日本語応答を強制する場合、システムプロンプトに追加
        if self.language == 'ja':
            self.system_prompt += "\n\n重要: 全ての応答は必ず日本語で行ってください。英語での応答は絶対に避けてください。"
        
        # Initialize Strands Agent with OpenAI model
        if Config.OPENAI_API_KEY:
            model_name = kwargs.get('model', Config.DEFAULT_MODEL)
            self.model = OpenAIModel(
                api_key=Config.OPENAI_API_KEY,
                model_id=model_name,
                temperature=kwargs.get('temperature', Config.DEFAULT_TEMPERATURE),
                max_tokens=kwargs.get('max_tokens', Config.DEFAULT_MAX_TOKENS)
            )
            self.agent = Agent(
                model=self.model,
                system_prompt=self.system_prompt
            )
        else:
            self.model = None
            self.agent = None
    
    @abstractmethod
    def process_query(self, query: str, context: Optional[Dict[str, Any]] = None) -> str:
        """Process a query and return a response.
        
        Args:
            query: The input query to process
            context: Optional context information
            
        Returns:
            The agent's response as a string
        """
        pass
    
    def call_llm(self, user_query: str) -> str:
        """Call the LLM with the given query.
        
        Args:
            user_query: The user's query
            
        Returns:
            The LLM's response
        """
        if not self.agent:
            return "Error: OpenAI API key not configured"
        
        try:
            # Use Strands Agent to process the query
            result = self.agent(user_query)
            
            # Extract text from AgentResult
            if hasattr(result, 'message') and isinstance(result.message, dict):
                # Handle Strands AgentResult format
                message = result.message
                if 'content' in message and isinstance(message['content'], list):
                    # Extract text from content list
                    for content_item in message['content']:
                        if isinstance(content_item, dict) and 'text' in content_item:
                            return content_item['text']
                elif 'content' in message:
                    return message['content']
            elif hasattr(result, 'content'):
                return result.content
            elif hasattr(result, 'text'):
                return result.text
            elif isinstance(result, str):
                return result
            else:
                return str(result)
        except Exception as e:
            return f"Error calling LLM: {str(e)}"
    
    def __str__(self) -> str:
        """String representation of the agent."""
        return f"{self.__class__.__name__}(name='{self.name}')"
    
    def __repr__(self) -> str:
        """Detailed string representation of the agent."""
        return f"{self.__class__.__name__}(name='{self.name}', system_prompt='{self.system_prompt[:50]}...')"

