"""Research Assistant Agent implementation."""

from typing import Any, Dict, Optional
from .base_agent import BaseAgent


class ResearchAssistant(BaseAgent):
    """Specialized agent for research and factual information queries."""
    
    SYSTEM_PROMPT = """あなたは専門的な研究アシスタントです。研究に関する質問に対して、事実に基づいた信頼できる情報のみを提供することに集中してください。

あなたの責務:
- 正確で包括的な研究回答を提供する
- 可能な限り出典を明記する
- 意見ではなく事実情報に焦点を当てる
- 複雑なトピックを理解しやすく分解して説明する
- さらなる学習のための追加リソースを提案する

常にプロフェッショナルで情報豊富なトーンを維持してください。"""
    
    def __init__(self, **kwargs):
        """Initialize the Research Assistant."""
        super().__init__(
            name="Research Assistant",
            system_prompt=self.SYSTEM_PROMPT,
            **kwargs
        )
    
    def process_query(self, query: str, context: Optional[Dict[str, Any]] = None) -> str:
        """Process a research-related query.
        
        Args:
            query: The research question to answer
            context: Optional context information
            
        Returns:
            A detailed research answer with citations
        """
        try:
            # Use LLM to process the research query
            research_prompt = f"""あなたは研究アシスタントとして、以下のクエリについて詳細で正確な情報を提供してください：

クエリ: {query}

以下の形式で回答してください：
1. 概要
2. 主要なポイント（箇条書き）
3. 詳細情報
4. 関連情報や追加の考察

必ず日本語で回答してください。"""
            
            return self.call_llm(research_prompt)
            
        except Exception as e:
            return f"Error in research assistant: {str(e)}"
    
    def _generate_research_response(self, query: str, context: Optional[Dict[str, Any]] = None) -> str:
        """Generate a research response (mock implementation).
        
        Args:
            query: The research question
            context: Optional context
            
        Returns:
            A formatted research response
        """
        # This is a mock implementation for demonstration
        # In a real system, this would integrate with Strands Agents
        
        response_template = f"""
## 研究回答: {query}

### 概要
利用可能な研究とドキュメントに基づいて、あなたの質問に対する包括的な回答をご提供します。

### 主な調査結果
- これは研究アシスタント機能を実証するモック応答です
- 実際の実装では、実際の研究データベースやAPIに接続します
- エージェントは適切な引用と共に、事実に基づいた信頼できる情報を提供します

### 詳細な分析
研究アシスタントは以下に関連するクエリを処理するよう設計されています：
- 技術文書と仕様
- 学術研究と論文
- 業界レポートと分析
- 歴史的情報と事実

### 出典と参考文献
- [モック出典 1]: 関連ドキュメント
- [モック出典 2]: 学術論文
- [モック出典 3]: 業界レポート

### さらなる読書のための推奨事項
このトピックに関するより詳細な情報については、以下をご検討ください：
- 関連する学術論文
- 公式ドキュメント
- 業界のホワイトペーパー

---
*研究アシスタントによって生成された回答*
        """.strip()
        
        return response_template

