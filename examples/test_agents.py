"""Test individual agents."""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from multi_agent_system.agents.research_assistant import ResearchAssistant
from multi_agent_system.agents.product_recommendation_assistant import ProductRecommendationAssistant
from multi_agent_system.agents.trip_planning_assistant import TripPlanningAssistant


def test_research_assistant():
    """Test the Research Assistant agent."""
    print("Testing Research Assistant")
    print("=" * 40)
    
    agent = ResearchAssistant()
    query = "What is artificial intelligence and how does it work?"
    
    print(f"Query: {query}")
    print()
    
    response = agent.process_query(query)
    print("Response:")
    print(response)
    print()


def test_product_recommendation_assistant():
    """Test the Product Recommendation Assistant agent."""
    print("Testing Product Recommendation Assistant")
    print("=" * 40)
    
    agent = ProductRecommendationAssistant()
    query = "I need a good smartphone for photography"
    context = {
        "budget": "$500-800",
        "preferences": ["good camera", "long battery life"]
    }
    
    print(f"Query: {query}")
    print(f"Context: {context}")
    print()
    
    response = agent.process_query(query, context)
    print("Response:")
    print(response)
    print()


def test_trip_planning_assistant():
    """Test the Trip Planning Assistant agent."""
    print("Testing Trip Planning Assistant")
    print("=" * 40)
    
    agent = TripPlanningAssistant()
    query = "Plan a weekend trip to Paris"
    context = {
        "duration": "3 days",
        "budget": "$1000",
        "interests": ["art", "food", "history"]
    }
    
    print(f"Query: {query}")
    print(f"Context: {context}")
    print()
    
    response = agent.process_query(query, context)
    print("Response:")
    print(response)
    print()


def main():
    """Run all agent tests."""
    print("Individual Agent Testing")
    print("=" * 60)
    print()
    
    # Test each agent
    test_research_assistant()
    print("=" * 60)
    print()
    
    test_product_recommendation_assistant()
    print("=" * 60)
    print()
    
    test_trip_planning_assistant()
    print("=" * 60)
    print()
    
    print("All agent tests completed!")


if __name__ == "__main__":
    main()

