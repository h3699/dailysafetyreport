import streamlit as st
from datetime import datetime

st.set_page_config(page_title="廣華醫院2期地盤安全報告", layout="wide")

st.markdown("""
<div style="text-align: center; margin-bottom: 20px;">
    <img src="https://raw.githubusercontent.com/h3699/dailysafetyreport/main/logo.png" width="280">
</div>
""", unsafe_allow_html=True)

st.title("中國水電 俊和")
st.subheader("廣華醫院2期地盤安全巡查報告系統")

st.success("✅ 工具已成功載入！")

st.info("目前為測試版，正在優化中...")

password = st.text_input("🔐 輸入安全密碼", type="password")
if password:
    st.success("密碼正確！工具即將完整開放。")
