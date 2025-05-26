"""
Base LLM Handler module for the Dental Agent Prototype.
This module provides the abstract base class for all LLM implementations.
"""

from abc import ABC, abstractmethod
from typing import Dict, Optional, Any

class BaseLLMHandler(ABC):
    def __init__(self, api_key: str, model_name: str):
        """
        Initialize the LLM handler.
        
        Args:
            api_key (str): API key for the LLM service
            model_name (str): Name of the model to use
        """
        self.api_key = api_key
        self.model_name = model_name
        self._validate_api_key()
        print(f"{self.__class__.__name__} initialized with model: {model_name}")

    @abstractmethod
    def _validate_api_key(self) -> None:
        """Validate the API key with the service."""
        pass

    @abstractmethod
    def generate_text(self, prompt: str, context: Optional[str] = None) -> str:
        """
        Generate text based on the prompt and optional context.
        
        Args:
            prompt (str): The input prompt
            context (Optional[str]): Additional context for the generation
            
        Returns:
            str: Generated text response
        """
        pass

    @abstractmethod
    def understand_intent(self, user_input: str) -> Dict[str, Any]:
        """
        Understand the intent and entities from user input.
        
        Args:
            user_input (str): The user's input text
            
        Returns:
            Dict[str, Any]: Dictionary containing intent and entities
        """
        pass

    @abstractmethod
    def query_knowledge_base(self, question: str) -> str:
        """
        Query the knowledge base with a question.
        
        Args:
            question (str): The question to ask
            
        Returns:
            str: Answer from the knowledge base
        """
        pass

    def _format_prompt(self, prompt: str, context: Optional[str] = None) -> str:
        """
        Format the prompt with context if provided.
        
        Args:
            prompt (str): The base prompt
            context (Optional[str]): Additional context
            
        Returns:
            str: Formatted prompt
        """
        if context:
            return f"Context: {context}\n\nPrompt: {prompt}"
        return prompt 