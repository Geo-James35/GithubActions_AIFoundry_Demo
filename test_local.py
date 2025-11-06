"""
Quick test script to verify the AI agent works locally
"""
import os
from agent.simple_agent import SimpleAIAgent

# You need to set these environment variables
# Replace with your actual values
AZURE_OPENAI_ENDPOINT = "YOUR_ENDPOINT_HERE"  # e.g., https://your-resource.openai.azure.com/
AZURE_OPENAI_KEY = "YOUR_KEY_HERE"  # Your OpenAI API key

def test_agent():
    print("🧪 Testing AI Agent Locally")
    print("=" * 50)
    
    # Check if environment variables are set
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT", AZURE_OPENAI_ENDPOINT)
    api_key = os.getenv("AZURE_OPENAI_KEY", AZURE_OPENAI_KEY)
    
    if "YOUR_ENDPOINT_HERE" in endpoint or "YOUR_KEY_HERE" in api_key:
        print("❌ Error: Please set your Azure OpenAI endpoint and key!")
        print("\nOption 1: Edit this file and replace the placeholder values")
        print("Option 2: Set environment variables:")
        print('  $env:AZURE_OPENAI_ENDPOINT="https://your-resource.openai.azure.com/"')
        print('  $env:AZURE_OPENAI_KEY="your-api-key"')
        return
    
    try:
        # Initialize the agent
        print(f"\n✅ Endpoint: {endpoint}")
        print("✅ API Key: [hidden]")
        print("\n🤖 Initializing agent...")
        
        agent = SimpleAIAgent(
            endpoint=endpoint,
            api_key=api_key,
            deployment_name="gpt-4o"
        )
        
        print("✅ Agent initialized!")
        
        # Test a simple question
        print("\n💬 Testing with a simple question...")
        test_message = "Say 'Hello from local testing!' if you're working correctly."
        print(f"User: {test_message}")
        
        response = agent.chat(test_message)
        print(f"\n🤖 Agent: {response}")
        
        print("\n" + "=" * 50)
        print("✅ SUCCESS! Your agent is working locally!")
        print("=" * 50)
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("\nCommon issues:")
        print("1. Check your endpoint URL is correct")
        print("2. Verify your API key is valid")
        print("3. Make sure gpt-4o is deployed in your Azure OpenAI resource")
        return False

if __name__ == "__main__":
    test_agent()
