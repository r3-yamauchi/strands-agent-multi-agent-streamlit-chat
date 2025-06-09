"""Quick start script for the multi-agent system."""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from multi_agent_system.orchestrator import OrchestratorAgent


def main():
    """Quick start demonstration."""
    print("🚀 Multi-Agent System - Quick Start")
    print("=" * 50)
    print()
    
    # Initialize the orchestrator
    orchestrator = OrchestratorAgent()
    
    print("✅ システムが正常に初期化されました")
    print()
    
    # Quick test queries
    test_queries = [
        "Hello! What can you help me with?",
        "Research artificial intelligence",
        "Recommend a good programming book",
        "Plan a trip to Tokyo"
    ]
    
    print("🧪 クイックテストを実行中...")
    print()
    
    for i, query in enumerate(test_queries, 1):
        print(f"テスト {i}: {query}")
        try:
            response = orchestrator.process_query(query)
            print("✅ 成功")
        except Exception as e:
            print(f"❌ エラー: {e}")
        print()
    
    print("🎉 すべてのテストが完了しました！")
    print()
    print("📖 詳細な使用方法:")
    print("  python examples/basic_usage.py      - 基本的な使用例")
    print("  python examples/advanced_usage.py   - 高度な使用例")
    print("  python tests/test_agents.py         - ユニットテスト")
    print()
    print("💡 インタラクティブモードを開始しますか？ (y/n): ", end="")
    
    try:
        choice = input().strip().lower()
        if choice in ['y', 'yes', 'はい']:
            print()
            print("🎭 インタラクティブモード開始")
            print("終了するには 'quit' と入力してください")
            print("-" * 40)
            
            while True:
                user_query = input("\nあなたの質問: ").strip()
                
                if user_query.lower() in ['quit', 'exit', 'q', '終了']:
                    print("👋 ありがとうございました！")
                    break
                
                if not user_query:
                    continue
                
                try:
                    response = orchestrator.process_query(user_query)
                    print("\n回答:")
                    print(response)
                    print("-" * 40)
                except Exception as e:
                    print(f"エラー: {e}")
        else:
            print("👋 お疲れ様でした！")
    
    except KeyboardInterrupt:
        print("\n👋 お疲れ様でした！")


if __name__ == "__main__":
    main()

