# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## プロジェクト概要

Strands Agentsを使用した「Agent as Tools」パターンによるマルチエージェントシステム。オーケストレーターが研究、製品推薦、旅行計画の専門エージェントを管理し、日本語と英語のクエリに対応。

**GitHubリポジトリ**: https://github.com/r3-yamauchi/strands-agent-multi-agent-streamlit-chat
**ライセンス**: MIT License

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
uv run python main.py                    # メインエントリーポイント
uv run python examples/basic_usage.py    # インタラクティブモード
uv run python examples/test_agents.py    # 個別エージェントテスト
uv run python examples/advanced_usage.py # 高度な使用例
```

### テスト
```bash
uv run python tests/test_agents.py       # 全ユニットテスト（17テスト）
uv run python tests/test_agents.py TestOrchestratorAgent  # 特定クラスのテスト
uv run python tests/test_agents.py TestOrchestratorAgent.test_multi_agent_coordination  # 特定メソッドのテスト
uv run python test_strands.py            # Strands統合テスト
uv run python test_trip_planning.py      # 旅行計画エージェントテスト
```

### 開発
```bash
uv sync --dev                            # 開発依存関係インストール
uv run black .                           # コードフォーマット
uv run flake8 .                          # スタイルチェック
```

### 仮想環境管理
```bash
# 仮想環境の再作成
rm -rf .venv
uv sync

# 仮想環境のアクティベート（uvを使わない場合）
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

### Gitブランチ戦略
- mainブランチ：安定版
- 機能ブランチ：`feature/機能名`で作成
- バグ修正：`fix/バグ名`で作成

## アーキテクチャ

### システム構成（Agent as Toolsパターン）
```
ユーザー入力 
    ↓
OrchestratorAgent (src/multi_agent_system/orchestrator.py)
    ├─ キーワード分析 (_analyze_query_and_select_tools)
    ├─ ツール選択 (AVAILABLE_TOOLS from agent_tools.py)
    └─ レスポンス統合 (_synthesize_responses)
          ↓
ツール関数 (src/multi_agent_system/tools/agent_tools.py)
    ├─ research_assistant_tool()
    ├─ product_recommendation_tool()
    └─ trip_planning_tool()
          ↓
専門エージェント (BaseAgent継承)
    ├─ ResearchAssistant
    ├─ ProductRecommendationAssistant
    └─ TripPlanningAssistant
          ↓
Strands Agent (OpenAIModel使用)
```

### Agent as Toolsパターンの実装
- 各エージェントはツール関数としてラップされ、オーケストレーターが呼び出す
- ツール関数は独立して呼び出し可能で、再利用性が高い
- 新しいエージェントの追加が容易（ツールとして登録するだけ）

### Strands Agents統合
- **BaseAgent**: `strands.Agent`と`strands.models.openai.OpenAIModel`を使用
- **モデル設定**: `model_id`パラメータでGPTモデルを指定（`model_name`ではない）
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
# 必須
OPENAI_API_KEY=your_openai_api_key_here

# オプション（デフォルト値）
DEFAULT_MODEL=gpt-4o                     # 使用するGPTモデル
DEFAULT_TEMPERATURE=0.7                  # 生成の創造性（0.0-1.0）
DEFAULT_MAX_TOKENS=16384                 # 最大トークン数（GPT-4o 2024-08-06版対応）
DEFAULT_LANGUAGE=ja                      # デフォルト言語（ja/en）

# AWS Bedrock（使用する場合）
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_DEFAULT_REGION=us-east-1
```

## 新規エージェント追加手順

1. **エージェントクラス作成** (`src/multi_agent_system/agents/new_agent.py`)
   - BaseAgentを継承
   - SYSTEM_PROMPTを定義
   - process_queryメソッドでcall_llmを使用

2. **ツール関数追加** (`src/multi_agent_system/tools/agent_tools.py`)
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
- Python 3.11以上が必要

### OpenAI API呼び出しエラー
- `.env`にOPENAI_API_KEYが設定されているか確認
- model_idパラメータ（model_nameではない）を使用
- APIキーの有効性を確認：`uv run python test_strands.py`
- モデル名が`gpt-4o`であることを確認（`gpt-3.5-turbo`ではない）

### 日本語クエリが認識されない
- agent_tools.pyのキーワードリストに日本語キーワードが含まれているか確認
- orchestrator.pyの_analyze_query_and_select_toolsでquery.lower()が使用されているか確認
- DEFAULT_LANGUAGE=jaが設定されているか確認

### Streamlit UIのエラー
- ポート8501が使用可能か確認
- `streamlit>=1.45.1`がインストールされているか確認
- `app.py`のasyncio関連エラーは同期実行に変更済み

### トークン数超過エラー
- GPT-4oの最大出力トークンは16,384
- 環境変数DEFAULT_MAX_TOKENSが適切に設定されているか確認
- 長い応答が必要な場合は、ユーザーに複数回に分けて質問するよう依頼


## プロジェクトファイル構成

### 主要ファイル
- `main.py`: コマンドライン実行のエントリーポイント
- `app.py`: Streamlit Web UIアプリケーション
- `quickstart.py`: 簡単な動作確認用スクリプト
- `src/multi_agent_system/agents/base_agent.py`: 全エージェントの基底クラス（Strands Agent統合）
- `src/multi_agent_system/orchestrator.py`: マルチエージェントオーケストレーター
- `src/multi_agent_system/tools/agent_tools.py`: エージェントのツール定義とキーワード設定

### ドキュメント
- `README.md`: プロジェクト概要と使い方、GitHubリポジトリ情報（https://github.com/r3-yamauchi/strands-agent-multi-agent-streamlit-chat）
- `LICENSE`: MITライセンスファイル

### 設定ファイル
- `.env.example`: 環境変数のテンプレート（GPT-4o、最大16384トークン設定済み）
- `pyproject.toml`: プロジェクト設定と依存関係定義
- `.flake8`: コードスタイルチェック設定
- `LICENSE`: MIT Licenseファイル

## デバッグとログ

### Strands Agentのレスポンス処理
```python
# AgentResultオブジェクトの構造を確認
result = agent(query)
print(f"Full result: {result}")
print(f"Message structure: {result.message}")
print(f"Text content: {result.message['content'][0]['text']}")
```

### エージェント選択のデバッグ
```python
# orchestrator.pyの_analyze_query_and_select_toolsメソッドで
# 選択されたツールを確認
print(f"Query: {query}")
print(f"Selected tools: {selected_tools}")
```

## パフォーマンス最適化

### エージェントのステートレス実装
- 各エージェントは独立したインスタンスとして動作
- コンテキストは`process_query`メソッドで明示的に渡す

### Streamlit UIでのセッション管理
- `st.session_state`でチャット履歴を管理
- エージェントインスタンスは毎回新規作成（状態を持たない）

### システムプロンプトの最適化
- 各エージェントのSYSTEM_PROMPTは簡潔に保つ
- 言語設定は`BaseAgent`で一元管理

### GPT-4oモデルの活用
- 高速レスポンスを活かしたリアルタイム応答
- 16,384トークンの出力を活用した詳細な回答
- マルチモーダル機能による将来的な拡張性

## 開発のベストプラクティス

### コード品質
- `black`でフォーマット統一
- `flake8`でスタイルチェック
- 型ヒントの積極的使用（Python 3.11+）

### Git管理
- `.env`ファイルは絶対にコミットしない
- APIキーは環境変数で管理
- `uv.lock`はコミットする（再現可能な環境のため）

### エージェント実装
- 新規エージェントは必ず`BaseAgent`を継承
- `call_llm`メソッドを使用してLLM呼び出しを統一
- エラーハンドリングは基底クラスで実装済み
- 複数のキーワードが含まれる場合、複数エージェントが選択される可能性あり
- より具体的なキーワードを使用して精度を向上
- 日本語対応は`language='ja'`パラメータで制御

### モデル設定の注意点
- デフォルトはGPT-4o（`gpt-4o`）を使用
- 最大トークン数は16,384（2024-08-06版対応）
- temperatureは0.7（バランスの取れた創造性）
- モデル指定時は`model_id`パラメータを使用（`model_name`ではない）


