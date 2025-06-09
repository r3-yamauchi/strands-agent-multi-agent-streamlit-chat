"""Agent tools for the multi-agent system."""

from typing import Any, Dict, Optional
from ..agents.research_assistant import ResearchAssistant
from ..agents.product_recommendation_assistant import ProductRecommendationAssistant
from ..agents.trip_planning_assistant import TripPlanningAssistant


def research_assistant_tool(query: str, context: Optional[Dict[str, Any]] = None) -> str:
    """
    Process and respond to research-related queries.
    
    This tool provides factual, well-sourced information in response to research questions.
    It focuses on academic research, technical documentation, and factual analysis.
    
    Args:
        query: A research question requiring factual information
        context: Optional context information for the research
    
    Returns:
        A detailed research answer with citations and sources
    """
    try:
        agent = ResearchAssistant()
        response = agent.process_query(query, context)
        return response
    except Exception as e:
        return f"Error in research assistant tool: {str(e)}"


def product_recommendation_tool(query: str, context: Optional[Dict[str, Any]] = None) -> str:
    """
    Provide personalized product recommendations and shopping advice.
    
    This tool analyzes user requirements and provides tailored product suggestions
    with detailed comparisons, pros/cons, and purchasing advice.
    
    Args:
        query: A product recommendation request
        context: Optional context (budget, preferences, requirements)
    
    Returns:
        Detailed product recommendations with analysis and comparisons
    """
    try:
        agent = ProductRecommendationAssistant()
        response = agent.process_query(query, context)
        return response
    except Exception as e:
        return f"Error in product recommendation tool: {str(e)}"


def trip_planning_tool(query: str, context: Optional[Dict[str, Any]] = None) -> str:
    """
    Create comprehensive travel itineraries and provide travel planning advice.
    
    This tool specializes in creating detailed travel plans, suggesting destinations,
    accommodations, activities, and providing practical travel advice.
    
    Args:
        query: A trip planning request
        context: Optional context (budget, dates, preferences, group size)
    
    Returns:
        A comprehensive travel itinerary with recommendations and practical information
    """
    try:
        agent = TripPlanningAssistant()
        response = agent.process_query(query, context)
        return response
    except Exception as e:
        return f"Error in trip planning tool: {str(e)}"


# Tool registry for easy access
AVAILABLE_TOOLS = {
    "research_assistant": {
        "function": research_assistant_tool,
        "description": "Process research-related queries and provide factual information",
        "keywords": ["research", "facts", "information", "study", "analysis", "documentation",
                     "研究", "調査", "情報", "調べ", "分析", "資料", "について", "とは"]
    },
    "product_recommendation": {
        "function": product_recommendation_tool,
        "description": "Provide product recommendations and shopping advice",
        "keywords": ["product", "recommendation", "shopping", "buy", "purchase", "compare",
                     "製品", "商品", "推薦", "推奨", "買い", "購入", "比較", "おすすめ"]
    },
    "trip_planning": {
        "function": trip_planning_tool,
        "description": "Create travel itineraries and provide trip planning advice",
        "keywords": ["travel", "trip", "vacation", "itinerary", "destination", "plan",
                     "旅行", "旅", "観光", "旅程", "行き先", "計画", "休暇", "バケーション"]
    }
}

