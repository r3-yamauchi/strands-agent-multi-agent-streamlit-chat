"""Basic usage example for the multi-agent system."""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from multi_agent_system.orchestrator import OrchestratorAgent


def main():
    """Demonstrate basic usage of the multi-agent system."""
    print("=" * 60)
    print("Multi-Agent System Demo")
    print("=" * 60)
    print()
    
    # Initialize the orchestrator
    orchestrator = OrchestratorAgent()
    
    # Test queries for different agents
    test_queries = [
        {
            "query": "Hello! What can you help me with?",
            "description": "Greeting and capabilities inquiry"
        },
        {
            "query": "Tell me about machine learning algorithms and their applications",
            "description": "Research query"
        },
        {
            "query": "Recommend a good laptop for programming and development work",
            "description": "Product recommendation query"
        },
        {
            "query": "Plan a 5-day trip to Tokyo with cultural activities and good food",
            "description": "Trip planning query"
        },
        {
            "query": "I need research on cloud computing and also want to buy a good book about it",
            "description": "Multi-agent query (research + product recommendation)"
        }
    ]
    
    # Process each test query
    for i, test in enumerate(test_queries, 1):
        print(f"Test {i}: {test['description']}")
        print("-" * 40)
        print(f"Query: {test['query']}")
        print()
        
        try:
            response = orchestrator.process_query(test['query'])
            print("Response:")
            print(response)
        except Exception as e:
            print(f"Error: {str(e)}")
        
        print()
        print("=" * 60)
        print()
    
    # Interactive mode
    print("Interactive Mode - Enter your queries (type 'quit' to exit):")
    print("-" * 60)
    
    while True:
        try:
            user_query = input("\nYour query: ").strip()
            
            if user_query.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            
            if not user_query:
                continue
            
            print("\nProcessing...")
            response = orchestrator.process_query(user_query)
            print("\nResponse:")
            print(response)
            print("-" * 40)
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()

