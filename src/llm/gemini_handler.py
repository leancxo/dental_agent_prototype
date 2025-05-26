"""
Gemini Handler module for the Dental Agent Prototype.
This module provides the implementation for Google's Gemini models.
"""

import google.generativeai as genai
from typing import Dict, Optional, Any
from .base_handler import BaseLLMHandler

class GeminiHandler(BaseLLMHandler):
    def __init__(self, api_key: str, model_name: str = "gemini-pro"):
        """
        Initialize the Gemini handler.
        
        Args:
            api_key (str): Google API key
            model_name (str): Name of the Gemini model to use (default: gemini-pro)
        """
        super().__init__(api_key, model_name)
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)

    def _validate_api_key(self) -> None:
        """Validate the Google API key."""
        try:
            # Make a simple API call to validate the key
            self.model.generate_content("Test")
        except Exception as e:
            raise ValueError(f"Invalid Google API key: {str(e)}")

    def generate_text(self, prompt: str, context: Optional[str] = None) -> str:
        """
        Generate text using Gemini.
        
        Args:
            prompt (str): The input prompt
            context (Optional[str]): Additional context for the generation
            
        Returns:
            str: Generated text response
        """
        formatted_prompt = self._format_prompt(prompt, context)
        
        try:
            response = self.model.generate_content(
                formatted_prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.7,
                    max_output_tokens=500,
                )
            )
            return response.text
        except Exception as e:
            print(f"Error generating text with Gemini: {str(e)}")
            return "I apologize, but I'm having trouble generating a response right now."

    def understand_intent(self, user_input: str) -> Dict[str, Any]:
        """
        Understand the intent and entities from user input using Gemini.
        
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
            response = self.model.generate_content(
                f"{system_prompt}\n\nUser input: {user_input}",
                generation_config=genai.types.GenerationConfig(
                    temperature=0.3,
                    max_output_tokens=150,
                )
            )
            # Parse the response as JSON
            import json
            return json.loads(response.text)
        except Exception as e:
            print(f"Error understanding intent with Gemini: {str(e)}")
            return {"intent": "unknown", "entities": {}}

    def query_knowledge_base(self, question: str) -> str:
        """
        Query the knowledge base using Gemini.
        
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
            response = self.model.generate_content(
                f"{system_prompt}\n\nQuestion: {question}",
                generation_config=genai.types.GenerationConfig(
                    temperature=0.5,
                    max_output_tokens=300,
                )
            )
            return response.text
        except Exception as e:
            print(f"Error querying knowledge base with Gemini: {str(e)}")
            return "I apologize, but I'm having trouble accessing the dental knowledge base right now." 