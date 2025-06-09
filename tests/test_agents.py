"""Unit tests for the multi-agent system."""

import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from multi_agent_system.agents.research_assistant import ResearchAssistant
from multi_agent_system.agents.product_recommendation_assistant import ProductRecommendationAssistant
from multi_agent_system.agents.trip_planning_assistant import TripPlanningAssistant
from multi_agent_system.orchestrator import OrchestratorAgent


class TestResearchAssistant(unittest.TestCase):
    """Test cases for Research Assistant."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.agent = ResearchAssistant()
    
    def test_initialization(self):
        """Test agent initialization."""
        self.assertEqual(self.agent.name, "Research Assistant")
        self.assertIn("research assistant", self.agent.system_prompt.lower())
    
    def test_process_query(self):
        """Test query processing."""
        query = "What is machine learning?"
        response = self.agent.process_query(query)
        
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)
        self.assertIn("Research Response", response)
    
    def test_process_query_with_context(self):
        """Test query processing with context."""
        query = "Explain neural networks"
        context = {"level": "beginner"}
        response = self.agent.process_query(query, context)
        
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)


class TestProductRecommendationAssistant(unittest.TestCase):
    """Test cases for Product Recommendation Assistant."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.agent = ProductRecommendationAssistant()
    
    def test_initialization(self):
        """Test agent initialization."""
        self.assertEqual(self.agent.name, "Product Recommendation Assistant")
        self.assertIn("product recommendation", self.agent.system_prompt.lower())
    
    def test_process_query(self):
        """Test query processing."""
        query = "Recommend a laptop"
        response = self.agent.process_query(query)
        
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)
        self.assertIn("Product Recommendations", response)
    
    def test_process_query_with_context(self):
        """Test query processing with context."""
        query = "Best smartphone for photography"
        context = {"budget": "$500", "preferences": ["camera"]}
        response = self.agent.process_query(query, context)
        
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)


class TestTripPlanningAssistant(unittest.TestCase):
    """Test cases for Trip Planning Assistant."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.agent = TripPlanningAssistant()
    
    def test_initialization(self):
        """Test agent initialization."""
        self.assertEqual(self.agent.name, "Trip Planning Assistant")
        self.assertIn("trip planning", self.agent.system_prompt.lower())
    
    def test_process_query(self):
        """Test query processing."""
        query = "Plan a trip to Tokyo"
        response = self.agent.process_query(query)
        
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)
        self.assertIn("Trip Planning", response)
    
    def test_process_query_with_context(self):
        """Test query processing with context."""
        query = "Weekend getaway"
        context = {"duration": "2 days", "budget": "$500"}
        response = self.agent.process_query(query, context)
        
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)


class TestOrchestratorAgent(unittest.TestCase):
    """Test cases for Orchestrator Agent."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.orchestrator = OrchestratorAgent()
    
    def test_initialization(self):
        """Test orchestrator initialization."""
        self.assertEqual(self.orchestrator.name, "Orchestrator Agent")
        self.assertIn("orchestrator", self.orchestrator.system_prompt.lower())
    
    def test_greeting_query(self):
        """Test greeting queries."""
        query = "Hello"
        response = self.orchestrator.process_query(query)
        
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)
        self.assertIn("Hello", response)
    
    def test_help_query(self):
        """Test help queries."""
        query = "What can you do?"
        response = self.orchestrator.process_query(query)
        
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)
        self.assertIn("Research Assistant", response)
        self.assertIn("Product Recommendation", response)
        self.assertIn("Trip Planning", response)
    
    def test_research_query(self):
        """Test research-related queries."""
        query = "Research artificial intelligence"
        response = self.orchestrator.process_query(query)
        
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)
        self.assertIn("Research Response", response)
    
    def test_product_query(self):
        """Test product recommendation queries."""
        query = "What should I buy for programming?"
        response = self.orchestrator.process_query(query)
        
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)
        self.assertIn("Product Recommendations", response)
    
    def test_travel_query(self):
        """Test travel planning queries."""
        query = "Plan a trip to Paris"
        response = self.orchestrator.process_query(query)
        
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)
        self.assertIn("Trip Planning", response)
    
    def test_multi_agent_query(self):
        """Test queries that require multiple agents."""
        query = "Research cloud computing and buy books about it"
        response = self.orchestrator.process_query(query)
        
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)
        # Check for either comprehensive response or single agent response
        self.assertTrue(
            "Comprehensive Response" in response or 
            "Research Response" in response or
            "Product Recommendations" in response
        )
    
    def test_get_available_tools(self):
        """Test getting available tools."""
        tools = self.orchestrator.get_available_tools()
        
        self.assertIsInstance(tools, dict)
        self.assertIn("research_assistant", tools)
        self.assertIn("product_recommendation", tools)
        self.assertIn("trip_planning", tools)


if __name__ == "__main__":
    # Run all tests
    unittest.main(verbosity=2)

