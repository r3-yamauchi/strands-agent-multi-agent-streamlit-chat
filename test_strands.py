#!/usr/bin/env python
"""Test script to verify Strands Agents integration."""

from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Test basic imports
try:
    from strands import Agent
    from strands.models.openai import OpenAIModel
    print("✅ Strands Agents imports successful")
except ImportError as e:
    print(f"❌ Import error: {e}")
    exit(1)

# Test OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("❌ OPENAI_API_KEY not found in environment")
    exit(1)
print("✅ OpenAI API key found")

# Test creating a model and agent
try:
    model = OpenAIModel(api_key=api_key, model_id="gpt-3.5-turbo")
    print("✅ OpenAI model created")
    
    agent = Agent(
        model=model,
        system_prompt="You are a helpful assistant. Always respond in Japanese."
    )
    print("✅ Agent created")
    
    # Test a simple query - try different method names
    try:
        # Try different possible method names
        if hasattr(agent, 'query'):
            response = agent.query("こんにちは。今日の天気はどうですか？")
        elif hasattr(agent, 'chat'):
            response = agent.chat("こんにちは。今日の天気はどうですか？")
        elif hasattr(agent, 'generate'):
            response = agent.generate("こんにちは。今日の天気はどうですか？")
        elif hasattr(agent, 'invoke'):
            response = agent.invoke("こんにちは。今日の天気はどうですか？")
        elif hasattr(agent, '__call__'):
            response = agent("こんにちは。今日の天気はどうですか？")
        else:
            print("Available methods:", [attr for attr in dir(agent) if not attr.startswith('_')])
            raise AttributeError("Could not find appropriate method to run query")
        # Debug response object
        print(f"Response type: {type(response)}")
        print(f"Response attributes: {[attr for attr in dir(response) if not attr.startswith('_')]}")
        
        # Handle different response types
        response_text = None
        if hasattr(response, 'content'):
            response_text = response.content
        elif hasattr(response, 'text'):
            response_text = response.text
        elif hasattr(response, 'message'):
            response_text = response.message
        elif hasattr(response, 'messages') and response.messages:
            # Get the last message
            last_message = response.messages[-1]
            if hasattr(last_message, 'content'):
                response_text = last_message.content
            else:
                response_text = str(last_message)
        elif isinstance(response, str):
            response_text = response
        else:
            response_text = str(response)
            
        print(f"✅ Agent response: {response_text}")
    except Exception as e:
        print(f"Error executing query: {e}")
        print("Agent attributes:", dir(agent))
    
except Exception as e:
    print(f"❌ Error: {e}")
    exit(1)

print("\n✅ All tests passed!")