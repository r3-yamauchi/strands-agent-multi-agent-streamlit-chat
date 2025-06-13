import streamlit as st
import asyncio
from dotenv import load_dotenv
import os
from src.multi_agent_system.orchestrator import OrchestratorAgent
from src.multi_agent_system.utils.config import Config

# ページ設定
st.set_page_config(
    page_title="Multi-Agent Chat System",
    page_icon="🤖",
    layout="centered"
)

# 環境変数の読み込み
load_dotenv()

# スタイルの適用
st.markdown("""
<style>
    .stChatMessage {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 0.5rem;
    }
    .agent-response {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-top: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# タイトルと説明
st.title("🤖 マルチエージェントチャット")
st.markdown("""
このシステムは、複数の専門エージェントがあなたの質問に答えます：
- 🔍 **研究アシスタント**: 情報調査や分析
- 🛍️ **製品推薦アシスタント**: 商品の推薦やレビュー
- ✈️ **旅行計画アシスタント**: 旅行の計画やアドバイス
""")

# セッション状態の初期化
if "messages" not in st.session_state:
    st.session_state.messages = []
if "orchestrator" not in st.session_state:
    with st.spinner("エージェントを初期化中..."):
        st.session_state.orchestrator = OrchestratorAgent()

# チャット履歴の表示
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "agent" in message:
            st.markdown(f"*応答元: {message['agent']}*")

# ユーザー入力
if prompt := st.chat_input("質問を入力してください..."):
    # ユーザーメッセージを追加
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # アシスタントの応答を生成
    with st.chat_message("assistant"):
        with st.spinner("考え中..."):
            try:
                # 同期的に実行
                response = st.session_state.orchestrator.process_query(prompt)
                
                # 応答を表示
                st.markdown(response["response"])
                agent_name = response.get("agent_used", "不明")
                st.markdown(f"*応答元: {agent_name}*")
                
                # メッセージを履歴に追加
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response["response"],
                    "agent": agent_name
                })
                
            except Exception as e:
                error_message = f"エラーが発生しました: {str(e)}"
                st.error(error_message)
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": error_message
                })

# サイドバーに情報を表示
with st.sidebar:
    st.header("📊 システム情報")
    st.info(f"会話数: {len(st.session_state.messages)}")
    
    if st.button("会話をクリア"):
        st.session_state.messages = []
        st.rerun()
    
    st.header("💡 使い方のヒント")
    st.markdown("""
    - **研究**: "〜について調べて"
    - **商品**: "〜を買いたい"、"〜の推薦"
    - **旅行**: "〜への旅行"、"〜の観光"
    """)
    
    # API設定の確認
    st.header("⚙️ API設定")
    if os.getenv("OPENAI_API_KEY"):
        st.success("✅ OpenAI API キー設定済み")
    else:
        st.warning("⚠️ OpenAI API キーが設定されていません")