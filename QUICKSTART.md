# Multi-Agent System - 実行ガイド

## 🚀 クイックスタート

### 1. 最速で試す方法

```bash
# プロジェクトを展開
unzip multi-agent-system.zip
cd multi-agent-system

# クイックスタート（推奨）
uv run python quickstart.py
```

### 2. 段階的なセットアップ

```bash
# 1. 仮想環境のセットアップ
uv sync

# 2. 基本的な使用例を実行
uv run python examples/basic_usage.py

# 3. テストを実行して動作確認
uv run python tests/test_agents.py
```

## 📋 実行可能なスクリプト一覧

| スクリプト | 説明 | 実行コマンド |
|-----------|------|-------------|
| `quickstart.py` | 最速で試せるクイックスタート | `uv run python quickstart.py` |
| `examples/basic_usage.py` | 基本的な使用例とインタラクティブモード | `uv run python examples/basic_usage.py` |
| `examples/advanced_usage.py` | 高度な使用例とデモ | `uv run python examples/advanced_usage.py` |
| `examples/test_agents.py` | 個別エージェントのテスト | `uv run python examples/test_agents.py` |
| `tests/test_agents.py` | ユニットテスト（17テスト） | `uv run python tests/test_agents.py` |

## 🎯 使用例

### 研究関連のクエリ
```
"機械学習アルゴリズムについて教えてください"
"量子コンピューティングの基礎を説明してください"
"ブロックチェーン技術の最新動向を調査してください"
```

### 商品推薦のクエリ
```
"プログラミング学習におすすめのノートパソコンを教えてください"
"写真撮影に適したスマートフォンを推薦してください"
"在宅ワーク用のオフィス機器を購入したいです"
```

### 旅行計画のクエリ
```
"東京での3日間の観光プランを作成してください"
"予算10万円でヨーロッパ旅行を計画してください"
"家族向けの沖縄旅行プランを提案してください"
```

### 複合クエリ（マルチエージェント）
```
"クラウドコンピューティングについて調べて、関連する良い書籍も推薦してください"
"持続可能な旅行について研究して、エコツーリズムの旅行プランも作成してください"
```

## 🔧 トラブルシューティング

### uvが見つからない場合
```bash
# uvをインストール
curl -LsSf https://astral.sh/uv/install.sh | sh
# または
pip install uv
```

### 依存関係のエラー
```bash
# 仮想環境をクリーンアップして再作成
rm -rf .venv
uv sync
```

### Pythonパスのエラー
```bash
# 仮想環境をアクティベート
source .venv/bin/activate  # Linux/macOS
# または
.venv\Scripts\activate     # Windows
```

## 📊 システム要件

- **Python**: 3.11以上
- **メモリ**: 最小512MB（推奨1GB以上）
- **ディスク**: 約50MB
- **OS**: Windows, macOS, Linux

## 🎉 成功の確認

すべてが正常に動作している場合：

1. ✅ `uv run python quickstart.py` が正常に実行される
2. ✅ テストが17個すべて成功する
3. ✅ インタラクティブモードで質問に回答が返される
4. ✅ 各エージェントが適切に選択される

問題がある場合は、エラーメッセージを確認して上記のトラブルシューティングを参照してください。

