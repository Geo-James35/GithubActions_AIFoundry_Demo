"""
Simple AI Agent for Azure AI Foundry Deployment Demo

This agent demonstrates a basic conversational AI that can be deployed
to Azure AI Foundry using GitHub Actions.
"""

import os
import json
from datetime import datetime
from typing import Dict, List, Optional
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential
from azure.identity import DefaultAzureCredential

# Version and deployment tracking
__version__ = "1.0.1"
__deployment_date__ = "2025-01-07"


class SimpleAIAgent:
    """
    A simple AI agent that uses Azure OpenAI for conversations.
    """
    
    def __init__(
        self,
        endpoint: Optional[str] = None,
        api_key: Optional[str] = None,
        deployment_name: str = "gpt-4o",
        system_prompt: Optional[str] = None
    ):
        """
        Initialize the AI agent.
        
        Args:
            endpoint: Azure OpenAI endpoint URL
            api_key: Azure OpenAI API key (if None, uses DefaultAzureCredential)
            deployment_name: Name of the deployed model
            system_prompt: System prompt for the agent
        """
        self.endpoint = endpoint or os.getenv("AZURE_OPENAI_ENDPOINT")
        self.deployment_name = deployment_name
        self.system_prompt = system_prompt or self._default_system_prompt()
        
        # Initialize the client
        if api_key or os.getenv("AZURE_OPENAI_KEY"):
            credential = AzureKeyCredential(api_key or os.getenv("AZURE_OPENAI_KEY"))
        else:
            credential = DefaultAzureCredential()
            
        self.client = ChatCompletionsClient(
            endpoint=self.endpoint,
            credential=credential
        )
        
        # Conversation history
        self.conversation_history: List[Dict] = [
            {"role": "system", "content": self.system_prompt}
        ]
    
    def _default_system_prompt(self) -> str:
        """Default system prompt for the agent."""
        return f"""You are a helpful AI assistant deployed on Azure AI Foundry.
You can answer questions, help with tasks, and engage in friendly conversation.
Be concise, helpful, and professional.

Agent Version: {__version__}
Last Deployment: {__deployment_date__}"""
    
    def get_version_info(self) -> Dict[str, str]:
        """Get version and deployment information."""
        return {
            "version": __version__,
            "deployment_date": __deployment_date__,
            "endpoint": self.endpoint,
            "model": self.deployment_name
        }
    
    def chat(self, user_message: str) -> str:
        """
        Send a message to the agent and get a response.
        
        Args:
            user_message: The user's message
            
        Returns:
            The agent's response
        """
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        try:
            # Call the model
            response = self.client.complete(
                messages=self.conversation_history,
                model=self.deployment_name,
                temperature=0.7,
                max_tokens=800
            )
            
            # Extract the response
            assistant_message = response.choices[0].message.content
            
            # Add to history
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            return assistant_message
            
        except Exception as e:
            error_message = f"Error communicating with the model: {str(e)}"
            print(error_message)
            return error_message
    
    def reset_conversation(self):
        """Reset the conversation history."""
        self.conversation_history = [
            {"role": "system", "content": self.system_prompt}
        ]
    
    def get_conversation_history(self) -> List[Dict]:
        """Get the current conversation history."""
        return self.conversation_history


def main():
    """
    Main function for testing the agent locally.
    """
    print("🤖 AI Foundry Agent Demo")
    print("=" * 50)
    
    # Initialize the agent
    try:
        agent = SimpleAIAgent()
        print("✅ Agent initialized successfully!")
        print(f"📍 Endpoint: {agent.endpoint}")
        print(f"🎯 Model: {agent.deployment_name}")
        print("\nType 'exit' to quit, 'reset' to start a new conversation\n")
        
        # Interactive loop
        while True:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() == 'exit':
                print("👋 Goodbye!")
                break
                
            if user_input.lower() == 'reset':
                agent.reset_conversation()
                print("🔄 Conversation reset!")
                continue
            
            # Get response
            response = agent.chat(user_input)
            print(f"\nAgent: {response}\n")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("\nMake sure you have set the following environment variables:")
        print("  - AZURE_OPENAI_ENDPOINT")
        print("  - AZURE_OPENAI_KEY (or use DefaultAzureCredential)")


if __name__ == "__main__":
    main()
