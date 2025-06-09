"""Advanced usage examples for the multi-agent system."""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from multi_agent_system.orchestrator import OrchestratorAgent


def demonstrate_research_capabilities():
    """Demonstrate research assistant capabilities."""
    print("=" * 60)
    print("Research Assistant Demonstration")
    print("=" * 60)
    
    orchestrator = OrchestratorAgent()
    
    research_queries = [
        "Explain the fundamentals of quantum computing",
        "What are the latest developments in artificial intelligence?",
        "Research the environmental impact of renewable energy",
        "Analyze the history and evolution of blockchain technology"
    ]
    
    for query in research_queries:
        print(f"\nQuery: {query}")
        print("-" * 40)
        response = orchestrator.process_query(query)
        print(response[:500] + "..." if len(response) > 500 else response)
        print()


def demonstrate_product_recommendations():
    """Demonstrate product recommendation capabilities."""
    print("=" * 60)
    print("Product Recommendation Demonstration")
    print("=" * 60)
    
    orchestrator = OrchestratorAgent()
    
    product_queries = [
        "What should I buy for a home office setup?",
        "Recommend the best laptop for machine learning",
        "I need to purchase a good camera for photography",
        "What are the best books for learning Python programming?"
    ]
    
    for query in product_queries:
        print(f"\nQuery: {query}")
        print("-" * 40)
        response = orchestrator.process_query(query)
        print(response[:500] + "..." if len(response) > 500 else response)
        print()


def demonstrate_trip_planning():
    """Demonstrate trip planning capabilities."""
    print("=" * 60)
    print("Trip Planning Demonstration")
    print("=" * 60)
    
    orchestrator = OrchestratorAgent()
    
    travel_queries = [
        "Plan a vacation to Japan for 10 days",
        "Create an itinerary for a business trip to New York",
        "I want to travel to Europe on a budget",
        "Plan a family vacation to Disney World"
    ]
    
    for query in travel_queries:
        print(f"\nQuery: {query}")
        print("-" * 40)
        response = orchestrator.process_query(query)
        print(response[:500] + "..." if len(response) > 500 else response)
        print()


def demonstrate_multi_agent_coordination():
    """Demonstrate multi-agent coordination."""
    print("=" * 60)
    print("Multi-Agent Coordination Demonstration")
    print("=" * 60)
    
    orchestrator = OrchestratorAgent()
    
    complex_queries = [
        "Research machine learning and recommend books and courses to buy",
        "I want to learn about sustainable travel and plan an eco-friendly trip",
        "Research the best programming languages and recommend development tools to purchase",
        "Study renewable energy technologies and plan a trip to visit solar farms"
    ]
    
    for query in complex_queries:
        print(f"\nQuery: {query}")
        print("-" * 40)
        response = orchestrator.process_query(query)
        print(response[:800] + "..." if len(response) > 800 else response)
        print()


def interactive_demo():
    """Interactive demonstration mode."""
    print("=" * 60)
    print("Interactive Multi-Agent System Demo")
    print("=" * 60)
    print("Available commands:")
    print("- 'research': Switch to research mode")
    print("- 'products': Switch to product recommendation mode")
    print("- 'travel': Switch to travel planning mode")
    print("- 'help': Show available capabilities")
    print("- 'quit': Exit the demo")
    print("-" * 60)
    
    orchestrator = OrchestratorAgent()
    
    while True:
        try:
            user_input = input("\nEnter your query or command: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Thank you for trying the multi-agent system!")
                break
            
            if user_input.lower() == 'help':
                response = orchestrator.process_query("What can you help me with?")
                print("\n" + response)
                continue
            
            if user_input.lower() == 'research':
                print("\nResearch mode activated. Ask me any research question!")
                continue
            
            if user_input.lower() == 'products':
                print("\nProduct recommendation mode activated. Tell me what you need to buy!")
                continue
            
            if user_input.lower() == 'travel':
                print("\nTravel planning mode activated. Where would you like to go?")
                continue
            
            if not user_input:
                continue
            
            print("\nProcessing your query...")
            response = orchestrator.process_query(user_input)
            print("\nResponse:")
            print(response)
            print("-" * 40)
            
        except KeyboardInterrupt:
            print("\n\nThank you for trying the multi-agent system!")
            break
        except Exception as e:
            print(f"Error: {str(e)}")


def main():
    """Run advanced demonstrations."""
    print("Advanced Multi-Agent System Demonstrations")
    print("=" * 60)
    
    demos = {
        "1": ("Research Capabilities", demonstrate_research_capabilities),
        "2": ("Product Recommendations", demonstrate_product_recommendations),
        "3": ("Trip Planning", demonstrate_trip_planning),
        "4": ("Multi-Agent Coordination", demonstrate_multi_agent_coordination),
        "5": ("Interactive Demo", interactive_demo),
        "6": ("Run All Demos", lambda: [demo() for _, demo in [
            ("Research", demonstrate_research_capabilities),
            ("Products", demonstrate_product_recommendations),
            ("Travel", demonstrate_trip_planning),
            ("Multi-Agent", demonstrate_multi_agent_coordination)
        ]])
    }
    
    while True:
        print("\nSelect a demonstration:")
        for key, (name, _) in demos.items():
            print(f"{key}. {name}")
        print("0. Exit")
        
        choice = input("\nEnter your choice (0-6): ").strip()
        
        if choice == "0":
            print("Goodbye!")
            break
        
        if choice in demos:
            name, demo_func = demos[choice]
            print(f"\nStarting {name}...")
            demo_func()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

