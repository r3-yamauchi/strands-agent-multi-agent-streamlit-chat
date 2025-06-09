#!/usr/bin/env python
"""Test trip planning with Japanese query."""

from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Test the full system
try:
    from src.multi_agent_system.orchestrator import OrchestratorAgent
    
    print("✅ Imports successful")
    print(f"✅ OpenAI API key: {'Set' if os.getenv('OPENAI_API_KEY') else 'Not set'}")
    
    # Create orchestrator
    orchestrator = OrchestratorAgent()
    print("✅ Orchestrator created")
    
    # Test query
    query = "10月に宮古島への旅行をしたい"
    print(f"\n🔍 Testing query: {query}")
    
    # Process query
    result = orchestrator.process_query(query)
    
    print(f"\n📌 Agent used: {result['agent_used']}")
    print(f"\n💬 Response:\n{result['response']}")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()