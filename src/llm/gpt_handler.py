"""
GPT Handler module for the Dental Agent Prototype.
This module provides the implementation for OpenAI's GPT models.
"""

import openai
from typing import Dict, Optional, Any
from .base_handler import BaseLLMHandler

class GPTHandler(BaseLLMHandler):
    def __init__(self, api_key: str, model_name: str = "gpt-4"):
        """
        Initialize the GPT handler.
        
        Args:
            api_key (str): OpenAI API key
            model_name (str): Name of the GPT model to use (default: gpt-4)
        """
        super().__init__(api_key, model_name)
        openai.api_key = api_key

    def _validate_api_key(self) -> None:
        """Validate the OpenAI API key."""
        try:
            # Make a simple API call to validate the key
            openai.models.list()
        except Exception as e:
            raise ValueError(f"Invalid OpenAI API key: {str(e)}")

    def generate_text(self, prompt: str, context: Optional[str] = None) -> str:
        """
        Generate text using GPT.
        
        Args:
            prompt (str): The input prompt
            context (Optional[str]): Additional context for the generation
            
        Returns:
            str: Generated text response
        """
        formatted_prompt = self._format_prompt(prompt, context)
        
        try:
            response = openai.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": "You are a helpful dental assistant."},
                    {"role": "user", "content": formatted_prompt}
                ],
                temperature=0.7,
                max_tokens=500
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error generating text with GPT: {str(e)}")
            return "I apologize, but I'm having trouble generating a response right now."

    def understand_intent(self, user_input: str) -> Dict[str, Any]:
        """
        Understand the intent and entities from user input using GPT.
        
        Args:
            user_input (str): The user's input text
            
        Returns:
            Dict[str, Any]: Dictionary containing intent and entities
        """
        system_prompt = """You are an intent classification system for a dental assistant.
        Analyze the user input and return a JSON object with:
        - intent: one of ['schedule_appointment', 'dental_question', 'cancel_appointment', 'modify_appointment', 'unknown']
        - entities: a dictionary containing relevant information like time, patient_name, etc.
        Return ONLY the JSON object, no other text."""

        try:
            response = openai.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.3,
                max_tokens=150
            )
            # Parse the response as JSON
            import json
            return json.loads(response.choices[0].message.content)
        except Exception as e:
            print(f"Error understanding intent with GPT: {str(e)}")
            return {"intent": "unknown", "entities": {}}

    def query_knowledge_base(self, question: str) -> str:
        """
        Query the knowledge base using GPT.
        
        Args:
            question (str): The question to ask
            
        Returns:
            str: Answer from the knowledge base
        """
        system_prompt = """You are a dental knowledge assistant. 
        Provide accurate, helpful information about dental care and procedures.
        Always include a disclaimer to consult a dentist for specific medical advice.
        Keep responses concise and clear."""

        try:
            response = openai.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": question}
                ],
                temperature=0.5,
                max_tokens=300
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error querying knowledge base with GPT: {str(e)}")
            return "I apologize, but I'm having trouble accessing the dental knowledge base right now." 