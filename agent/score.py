"""
Scoring script for Azure AI Foundry deployment.
This script is called by Azure ML to handle inference requests.
"""

import json
import os
from simple_agent import SimpleAIAgent


# Global agent instance
agent = None


def init():
    """
    This function is called when the container is initialized/started.
    Initialize your model and any other required objects here.
    """
    global agent
    
    print("Initializing AI Foundry Agent...")
    
    # Get configuration from environment variables
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    deployment_name = os.getenv("DEPLOYMENT_NAME", "gpt-4o")
    
    # Initialize the agent
    agent = SimpleAIAgent(
        endpoint=endpoint,
        deployment_name=deployment_name
    )
    
    print("✅ Agent initialized successfully!")


def run(raw_data):
    """
    This function is called for every invocation of the endpoint.
    
    Args:
        raw_data: The raw request data as a string
        
    Returns:
        JSON response with the agent's reply
    """
    global agent
    
    try:
        # Parse the input
        data = json.loads(raw_data)
        user_message = data.get("message", "")
        reset = data.get("reset", False)
        
        # Validate input
        if not user_message and not reset:
            return json.dumps({
                "error": "No message provided",
                "status": "error"
            })
        
        # Reset conversation if requested
        if reset:
            agent.reset_conversation()
            return json.dumps({
                "message": "Conversation reset",
                "status": "success"
            })
        
        # Get response from agent
        response = agent.chat(user_message)
        
        # Return the response
        return json.dumps({
            "response": response,
            "status": "success",
            "conversation_length": len(agent.get_conversation_history())
        })
        
    except Exception as e:
        error_message = f"Error processing request: {str(e)}"
        print(error_message)
        return json.dumps({
            "error": error_message,
            "status": "error"
        })
