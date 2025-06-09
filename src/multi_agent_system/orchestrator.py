"""Orchestrator Agent implementation."""

from typing import Any, Dict, Optional, List
from .agents.base_agent import BaseAgent
from .tools.agent_tools import AVAILABLE_TOOLS


class OrchestratorAgent(BaseAgent):
    """Main orchestrator agent that coordinates specialized agents."""
    
    SYSTEM_PROMPT = """あなたは、ユーザーのクエリに包括的な応答を提供するために、専門的なAIアシスタントを調整する知的なオーケストレーターエージェントです。

あなたの責務:
- ユーザーのクエリを分析して、意図と要件を理解する
- クエリを処理するのに最適な専門エージェントを決定する
- 複雑なクエリのために必要に応じて複数のエージェントを調整する
- 複数のエージェントからの応答を一貫性のある包括的な回答に統合する
- 専門エージェントを必要としない簡単なクエリには直接応答する

利用可能な専門エージェント:
1. 研究アシスタント - 事実情報、研究、ドキュメントのクエリ用
2. 製品推奨アシスタント - 製品提案とショッピングアドバイス用  
3. 旅行計画アシスタント - 旅行計画と旅程作成用

ガイドライン:
- 専門知識に一致するクエリには専門エージェントを使用する
- 複雑なクエリでは、複数のエージェントを使用して応答を組み合わせることができる
- 簡単な会話クエリの場合は、専門エージェントを使用せずに直接応答する
- 常に役立つ、正確、そしてよく構造化された応答を提供する
- 情報が専門エージェントから来る場合は明確に示す"""
    
    def __init__(self, **kwargs):
        """Initialize the Orchestrator Agent."""
        super().__init__(
            name="Orchestrator Agent",
            system_prompt=self.SYSTEM_PROMPT,
            **kwargs
        )
        self.tools = AVAILABLE_TOOLS
    
    def process_query(self, query: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Process a user query by coordinating appropriate specialized agents.
        
        Args:
            query: The user's query
            context: Optional context information
            
        Returns:
            A dictionary containing the response and metadata
        """
        try:
            # Analyze the query to determine which tools to use
            selected_tools = self._analyze_query_and_select_tools(query)
            
            if not selected_tools:
                # Handle simple queries directly
                return {
                    "response": self._handle_direct_query(query),
                    "agent_used": "Orchestrator"
                }
            
            # Process with selected tools
            responses = self._process_with_tools(query, selected_tools, context)
            
            # Synthesize the final response
            final_response = self._synthesize_responses(query, responses)
            
            # Determine which agent was used
            agent_used = "Multiple Agents" if len(selected_tools) > 1 else selected_tools[0].replace("_", " ").title()
            
            return {
                "response": final_response,
                "agent_used": agent_used
            }
            
        except Exception as e:
            return {
                "response": f"Error in orchestrator agent: {str(e)}",
                "agent_used": "Orchestrator"
            }
    
    def _analyze_query_and_select_tools(self, query: str) -> List[str]:
        """Analyze the query and select appropriate tools.
        
        Args:
            query: The user's query
            
        Returns:
            List of tool names to use
        """
        query_lower = query.lower()
        selected_tools = []
        
        # Simple keyword-based tool selection
        for tool_name, tool_info in self.tools.items():
            keywords = tool_info["keywords"]
            if any(keyword in query_lower for keyword in keywords):
                selected_tools.append(tool_name)
        
        return selected_tools
    
    def _process_with_tools(self, query: str, tool_names: List[str], context: Optional[Dict[str, Any]] = None) -> Dict[str, str]:
        """Process the query with selected tools.
        
        Args:
            query: The user's query
            tool_names: List of tool names to use
            context: Optional context information
            
        Returns:
            Dictionary mapping tool names to their responses
        """
        responses = {}
        
        for tool_name in tool_names:
            if tool_name in self.tools:
                tool_function = self.tools[tool_name]["function"]
                try:
                    response = tool_function(query, context)
                    responses[tool_name] = response
                except Exception as e:
                    responses[tool_name] = f"Error using {tool_name}: {str(e)}"
        
        return responses
    
    def _synthesize_responses(self, query: str, responses: Dict[str, str]) -> str:
        """Synthesize responses from multiple tools into a coherent answer.
        
        Args:
            query: The original user query
            responses: Dictionary of tool responses
            
        Returns:
            Synthesized final response
        """
        if len(responses) == 1:
            # Single tool response
            tool_name, response = next(iter(responses.items()))
            return f"## 回答: {query}\n\n{response}"
        
        elif len(responses) > 1:
            # Multiple tool responses - combine them
            synthesized = f"## 包括的な回答: {query}\n\n"
            synthesized += "包括的な回答を提供するために、複数の専門アシスタントに相談しました：\n\n"
            
            for i, (tool_name, response) in enumerate(responses.items(), 1):
                tool_display_name = tool_name.replace("_", " ").title()
                synthesized += f"### {i}. {tool_display_name}\n\n{response}\n\n"
            
            synthesized += "---\n*オーケストレーターエージェントによって調整された回答*"
            return synthesized
        
        else:
            # No tool responses - shouldn't happen if we reach this point
            return self._handle_direct_query(query)
    
    def _handle_direct_query(self, query: str) -> str:
        """Handle queries that don't require specialized agents.
        
        Args:
            query: The user's query
            
        Returns:
            Direct response from the orchestrator
        """
        # Simple conversational responses for common queries
        query_lower = query.lower()
        
        # Check if this should be handled by a specialized agent
        for tool_name, tool_info in self.tools.items():
            keywords = tool_info["keywords"]
            if any(keyword in query_lower for keyword in keywords):
                # This should have been handled by specialized agent
                return f"申し訳ございません。システムの設定に問題があるようです。クエリ: '{query}' は {tool_name} で処理されるべきでした。"
        
        if any(greeting in query_lower for greeting in ["hello", "hi", "hey", "good morning", "good afternoon", "こんにちは", "おはよう", "こんばんは"]):
            return """こんにちは！私はあなたのAIアシスタントオーケストレーターです。以下のようなお手伝いができます：

- **研究に関する質問** - 研究スペシャリストにおつなぎします
- **製品推奨** - ショッピングエキスパートが適切な製品を見つけるお手伝いをします
- **旅行計画** - 旅行スペシャリストが詳細な旅程を作成します

本日はどのようなお手伝いをご希望でしょうか？"""
        
        elif any(help_word in query_lower for help_word in ["help", "what can you do", "capabilities", "ヘルプ", "できること", "機能"]):
            return """私はさまざまなタスクであなたを助けるために、専門的なAIアシスタントを調整するオーケストレーターエージェントです：

## 利用可能なスペシャリスト:

### 🔍 研究アシスタント
- 事実情報と研究
- 技術文書
- 学術および業界分析
- 出典と参考文献

### 🛍️ 製品推奨アシスタント  
- パーソナライズされた製品提案
- 比較分析
- 予算を意識した推奨
- ショッピングアドバイスとヒント

### ✈️ 旅行計画アシスタント
- 包括的な旅行旅程
- 目的地の推奨
- 宿泊施設とアクティビティの提案
- 予算計画と実用的なヒント

## 仕組み:
1. あなたが質問をしたり、リクエストをする
2. 私がクエリを分析し、最も助けになるスペシャリストを決定する
3. 適切なエージェントと調整する
4. 包括的でよく整理された応答を提供する

以下のような質問を試してみてください：
- "機械学習アルゴリズムについて教えて" (研究)
- "プログラミング用の良いラップトップを推奨して" (製品)
- "東京への5日間の旅行を計画して" (旅行)"""
        
        else:
            return f"""あなたの質問を理解しました: "{query}"

このクエリに最適な専門アシスタントがどれかわかりません。ガイドを提供させてください：

- **事実情報や研究**については、"研究"、"についての情報"、"説明"のような単語で言い換えてみてください
- **製品推奨**については、"推奨"、"最適な製品"、"何を買うべき"のような単語を含めてください
- **旅行計画**については、"旅行"、"旅"、"休暇"、"旅程"を言及してください

また、私が何をお手伝いできるか直接聞いていただければ、私の機能についてより詳細な情報を提供します。"""
    
    def get_available_tools(self) -> Dict[str, Dict[str, Any]]:
        """Get information about available tools.
        
        Returns:
            Dictionary of available tools and their information
        """
        return self.tools

