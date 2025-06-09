# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## プロジェクト概要

Strands Agentsを使用した「Agent as Tools」パターンによるマルチエージェントシステム。オーケストレーターが研究、製品推薦、旅行計画の専門エージェントを管理し、日本語と英語のクエリに対応。

## 重要なコマンド

### セットアップ
```bash
# Python 3.11+ と uv が必要
uv sync                                  # 仮想環境作成と依存関係インストール
cp .env.example .env                     # 環境変数設定ファイル作成
# .envにOPENAI_API_KEYを設定
```

### 実行
```bash
uv run streamlit run app.py              # Streamlit Web UI（推奨）
uv run python quickstart.py              # クイックスタート
uv run python examples/basic_usage.py    # インタラクティブモード
uv run python examples/test_agents.py    # 個別エージェントテスト
```

### テスト
```bash
uv run python tests/test_agents.py       # 全ユニットテスト
uv run python tests/test_agents.py TestOrchestratorAgent  # 特定クラスのテスト
uv run python test_strands.py            # Strands統合テスト
uv run python test_trip_planning.py      # 旅行計画エージェントテスト
```

### 開発
```bash
uv sync --dev                            # 開発依存関係インストール
uv run black .                           # コードフォーマット
uv run flake8 .                          # スタイルチェック
```

## アーキテクチャ

### システム構成
```
ユーザー入力 
    ↓
OrchestratorAgent (orchestrator.py)
    ├─ キーワード分析 (_analyze_query_and_select_tools)
    ├─ ツール選択 (AVAILABLE_TOOLS from agent_tools.py)
    └─ レスポンス統合 (_synthesize_responses)
          ↓
専門エージェント (BaseAgent継承)
    ├─ ResearchAssistant
    ├─ ProductRecommendationAssistant
    └─ TripPlanningAssistant
          ↓
Strands Agent (OpenAIModel使用)
```

### Strands Agents統合
- **BaseAgent**: `strands.Agent`と`strands.models.openai.OpenAIModel`を使用
- **LLM呼び出し**: `agent(query)`でAgentResultオブジェクトを取得
- **レスポンス抽出**: `result.message['content'][0]['text']`形式で処理

### キーワードベースルーティング
```python
# agent_tools.py の AVAILABLE_TOOLS
"research_assistant": {
    "keywords": ["research", "研究", "調査", "について", ...]
}
"product_recommendation": {
    "keywords": ["product", "製品", "商品", "買い", ...]
}
"trip_planning": {
    "keywords": ["travel", "旅行", "旅", "観光", ...]
}
```

### 環境変数
```bash
OPENAI_API_KEY=必須
DEFAULT_MODEL=gpt-3.5-turbo (デフォルト)
DEFAULT_LANGUAGE=ja
```

## 新規エージェント追加手順

1. **エージェントクラス作成** (`agents/new_agent.py`)
   - BaseAgentを継承
   - SYSTEM_PROMPTを定義
   - process_queryメソッドでcall_llmを使用

2. **ツール関数追加** (`tools/agent_tools.py`)
   ```python
   def new_agent_tool(query: str, context: Optional[Dict[str, Any]] = None) -> str:
       agent = NewAgent()
       return agent.process_query(query, context)
   ```

3. **AVAILABLE_TOOLSに登録**
   - 関数、説明、キーワード（日英両方）を追加

## トラブルシューティング

### strands_agents ImportError
- `uv sync`で依存関係を再インストール
- `strands-agents[openai]>=0.1.6`が必要

### OpenAI API呼び出しエラー
- `.env`にOPENAI_API_KEYが設定されているか確認
- model_idパラメータ（model_nameではない）を使用

### 日本語クエリが認識されない
- agent_tools.pyのキーワードリストに日本語キーワードが含まれているか確認
- orchestrator.pyの_analyze_query_and_select_toolsでquery.lower()が使用されているか確認