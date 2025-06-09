# Strands Agentsを使用したマルチエージェントシステム

このプロジェクトは、Strands Agentsライブラリを使用した「Agent as Tools」パターンによるマルチエージェントシステムです。オーケストレーターエージェントが複数の専門エージェントを調整し、ユーザーのクエリに対して適切な回答を提供します。

## 実行方法

```bash
# uvを使用して実行
uv run streamlit run app.py
```

## 🎯 アプリケーション概要

### システムアーキテクチャ

このマルチエージェントシステムは、1つのオーケストレーターエージェントが3つの専門エージェントを調整する階層構造を採用しています：

```
ユーザー
    ↓
オーケストレーターエージェント
    ↓
┌─────────────────┬─────────────────┬─────────────────┐
│ Research        │ Product         │ Trip Planning   │
│ Assistant       │ Recommendation  │ Assistant       │
│                 │ Assistant       │                 │
└─────────────────┴─────────────────┴─────────────────┘
```

### 専門エージェント

#### 🔍 研究アシスタント
- **専門分野**: 研究・調査・技術文書
- **機能**: 
  - 事実に基づく情報提供
  - 学術研究と技術仕様の説明
  - ソースと引用の提供
  - 詳細な分析レポート作成

#### 🛍️ 製品推薦アシスタント
- **専門分野**: 商品推薦・ショッピングアドバイス
- **機能**:
  - パーソナライズされた商品提案
  - 予算とニーズに基づく比較分析
  - 購入ガイダンスとアドバイス
  - 代替商品と補完商品の提案

#### ✈️ 旅行計画アシスタント
- **専門分野**: 旅行計画・旅程作成
- **機能**:
  - 包括的な旅行プラン作成
  - 宿泊・交通・アクティビティの提案
  - 予算計画と実用的なアドバイス
  - 地域情報と文化的なヒント

#### 🎭 オーケストレーターエージェント
- **役割**: メインコーディネーター
- **機能**:
  - ユーザークエリの分析と理解
  - 適切な専門エージェントの選択
  - 複数エージェントの調整
  - 応答の統合と最終出力の生成

### 主な特徴

- **🤖 Strands Agents統合**: OpenAI GPTモデルを使用した高度な自然言語処理
- **🌐 多言語対応**: 日本語と英語のクエリに対応
- **🔄 自動エージェント選択**: キーワードベースでクエリを分析し、最適なエージェントを自動選択
- **🤝 マルチエージェント協調**: 複雑なクエリに対して複数エージェントが連携して回答
- **🧩 モジュラー設計**: 新しいエージェントの追加や既存機能の拡張が容易
- **🛡️ エラーハンドリング**: 包括的なエラー処理とユーザーフレンドリーなメッセージ

## 🚀 セットアップと実行方法

### 前提条件

- **Python**: 3.11以上
- **uv**: Python パッケージマネージャー（推奨）
- **OpenAI APIキー**: Strands Agentsを通じてGPTモデルを使用

### uvのインストール

uvがインストールされていない場合：

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# pipを使用する場合
pip install uv
```

### プロジェクトのセットアップ

1. **リポジトリのクローン**:
```bash
git clone <repository-url>
cd multi-agent-system-strands-agent-chat
```

2. **仮想環境の作成と依存関係のインストール**:
```bash
# uvを使用した自動セットアップ
uv sync

# 環境変数の設定
cp .env.example .env
# .envファイルを編集してOPENAI_API_KEYを設定
```

### 実行方法

#### 1. Streamlit Web UIの起動（推奨）

```bash
# uvを使用して実行
uv run streamlit run app.py

# または仮想環境をアクティベートして実行
source .venv/bin/activate
streamlit run app.py
```

ブラウザで `http://localhost:8501` にアクセスしてチャットUIを使用できます。

#### 2. 基本的な使用例（CLI）

```bash
# uvを使用して実行
uv run python examples/basic_usage.py

# または仮想環境をアクティベートして実行
source .venv/bin/activate
python examples/basic_usage.py
```

#### 3. 個別エージェントのテスト

```bash
uv run python examples/test_agents.py
```

#### 4. 高度な使用例とデモ

```bash
uv run python examples/advanced_usage.py
```

#### 5. ユニットテストの実行

```bash
uv run python tests/test_agents.py
```

### 必要な環境変数

`.env`ファイルに以下を設定：

```bash
OPENAI_API_KEY=your_openai_api_key_here
DEFAULT_MODEL=gpt-3.5-turbo  # オプション、デフォルトはgpt-3.5-turbo
DEFAULT_LANGUAGE=ja          # オプション、デフォルトは日本語
```

## 💡 使用例

### 基本的なクエリ例

```python
from src.multi_agent_system.orchestrator import OrchestratorAgent

# オーケストレーターを初期化
orchestrator = OrchestratorAgent()

# 研究関連のクエリ
result = orchestrator.process_query("機械学習アルゴリズムについて教えてください")
print(f"使用エージェント: {result['agent_used']}")
print(f"回答: {result['response']}")

# 商品推薦のクエリ
result = orchestrator.process_query("プログラミング学習におすすめのノートパソコンを教えてください")

# 旅行計画のクエリ
result = orchestrator.process_query("東京での3日間の観光プランを作成してください")

# 複合クエリ（複数エージェント連携）
result = orchestrator.process_query("クラウドコンピューティングについて調べて、関連する良い書籍も推薦してください")
```

### インタラクティブモード

```bash
uv run python examples/basic_usage.py
```

実行すると、対話型インターフェースが起動し、以下のような専門エージェントが利用できます：

- **研究アシスタント**: 技術的な質問や調査依頼に対応
- **製品推薦アシスタント**: 商品選びや購入アドバイスを提供
- **旅行計画アシスタント**: 詳細な旅程や観光プランを作成

クエリに含まれるキーワードに基づいて、適切なエージェントが自動的に選択されます。

## 🧪 テストとデバッグ

### テストの実行

```bash
# 全テストの実行
uv run python tests/test_agents.py

# 個別エージェントのテスト
uv run python examples/test_agents.py
```

### テスト項目

- ✅ 各エージェントの初期化テスト
- ✅ クエリ処理機能のテスト
- ✅ 日本語・英語クエリのテスト
- ✅ Strands Agents統合テスト
- ✅ オーケストレーター機能のテスト
- ✅ マルチエージェント協調のテスト
- ✅ エラーハンドリングのテスト

## 📁 プロジェクト構造

```
multi-agent-system/
├── app.py                               # Streamlit Web UIアプリケーション
├── src/
│   └── multi_agent_system/
│       ├── __init__.py
│       ├── orchestrator.py              # メインオーケストレーター
│       ├── agents/
│       │   ├── __init__.py
│       │   ├── base_agent.py            # ベースエージェントクラス
│       │   ├── research_assistant.py    # 研究アシスタント
│       │   ├── product_recommendation_assistant.py  # 商品推薦アシスタント
│       │   └── trip_planning_assistant.py  # 旅行計画アシスタント
│       ├── tools/
│       │   ├── __init__.py
│       │   └── agent_tools.py           # エージェントツール
│       └── utils/
│           ├── __init__.py
│           └── config.py                # 設定管理
├── tests/
│   └── test_agents.py                   # ユニットテスト
├── examples/
│   ├── basic_usage.py                   # 基本的な使用例
│   ├── test_agents.py                   # エージェントテスト
│   └── advanced_usage.py                # 高度な使用例
├── pyproject.toml                       # プロジェクト設定
├── README.md                            # このファイル
├── DEVELOPMENT_GUIDE.md                 # 開発ガイド
└── .env.example                         # 環境変数サンプル
```

## 🔧 カスタマイズと拡張

### 新しいエージェントの追加

1. `src/multi_agent_system/agents/`に新しいエージェントクラスを作成
2. `BaseAgent`を継承し、`process_query`メソッドを実装
3. `src/multi_agent_system/tools/agent_tools.py`にツール関数を追加
4. オーケストレーターのツールレジストリに登録

### Strands Agentsの設定

各エージェントはStrands Agentsを使用してOpenAI GPTモデルと通信します。以下の設定が可能です：

- **モデルの変更**: `DEFAULT_MODEL`環境変数でGPTモデルを指定
- **システムプロンプト**: 各エージェントの`SYSTEM_PROMPT`を編集
- **言語設定**: `DEFAULT_LANGUAGE`でデフォルト言語を設定

### キーワードの追加

`agent_tools.py`の`AVAILABLE_TOOLS`に新しいキーワードを追加することで、エージェント選択の精度を向上させることができます。

## 🐛 トラブルシューティング

### よくある問題

1. **ModuleNotFoundError**: 
   ```bash
   uv sync
   ```

2. **OpenAI APIエラー**:
   - `.env`ファイルにOPENAI_API_KEYが設定されているか確認
   - APIキーが有効か確認

3. **エージェント選択が正しく動作しない**:
   - 日本語クエリの場合: "研究", "購入", "旅行"などのキーワードを含める
   - 英語クエリの場合: "research", "buy", "travel"などのキーワードを含める

4. **Strands Agentsインポートエラー**:
   ```bash
   uv sync  # strands-agents[openai]>=0.1.6がインストールされる
   ```

### デバッグ方法

```bash
# Strands統合のテスト
uv run python test_strands.py

# 特定エージェントのテスト
uv run python test_trip_planning.py
```

## 📚 参考資料

- [Strands Agentsドキュメント](https://github.com/strands-agents/strands)
- [OpenAI APIドキュメント](https://platform.openai.com/docs)
- [uvドキュメント](https://docs.astral.sh/uv/)
- [AWSワークショップ - Agent as a Tool](https://catalog.us-east-1.prod.workshops.aws/workshops/33f099a6-45a2-47d7-9e3c-a23a6568821e/ja-JP/20-multi-agent-topology/20a-agent-as-a-tool)

## 📄 ライセンス

MIT License

## 🤝 コントリビューション

改善提案やバグ報告は歓迎します。IssueやPull Requestをお待ちしています。

## 🔒 セキュリティ

- APIキーは`.env`ファイルに保存し、`.gitignore`に含めてください
- 本番環境では環境変数またはシークレット管理サービスを使用してください

