import streamlit as st
from docx import Document
from docx.shared import Inches
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="廣華醫院2期地盤安全報告", layout="wide")

# Logo (假設你已上傳 logo.png)
st.markdown("""
<div style="text-align: center; margin-bottom: 10px;">
    <img src="https://raw.githubusercontent.com/h3699/dailysafetyreport/main/logo.png" width="300">
</div>
""", unsafe_allow_html=True)

st.title("中國水電 俊和")
st.subheader("廣華醫院2期地盤安全巡查報告系統")

company = "中國水電 俊和"
site_name = "廣華醫院2期地盤"

# 密碼保護 (保持不變)
password = st.text_input("🔐 輸入安全密碼", type="password")
if not password or password != st.secrets["general"]["password"]:
    if password:
        st.error("❌ 密碼錯誤！")
    st.stop()

categories = ["地盤整潔", "機械", "個人防護", "吊運", "高空工作", "離地工作", "電力安全", "分判管理", "通道"]

if 'issues' not in st.session_state:
    st.session_state.issues = []
if 'history' not in st.session_state:
    st.session_state.history = []

tab1, tab2, tab3 = st.tabs(["新增問題", "生成報告", "歷史記錄"])

with tab1:
    st.subheader("新增安全問題")
    
    # 地盤分區地圖上傳
    st.write("**上傳地盤分區地圖**")
    map_image = st.file_uploader("上傳地圖 (jpg/png)", type=["jpg", "jpeg", "png"], key="map_upload")
    if map_image:
        st.image(map_image, width=700, caption="地盤分區地圖")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        date = st.date_input("巡查日期", datetime.today())
        location = st.text_input("發生地點（例如 Wing A - 2樓、圖上標記位置）")
        subcontractor = st.text_input("分判")
        category = st.selectbox("問題分類", categories)
        severity = st.selectbox("嚴重度", ["高", "中", "低"])
    
    with col2:
        problem = st.text_area("問題事項描述")
        suggestion = st.text_area("建議處理方法")
    
    uploaded_files = st.file_uploader("上傳問題相片", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
    
    if st.button("✅ 新增此問題", type="primary"):
        if problem.strip() and location.strip():
            st.session_state.issues.append({
                "date": date,
                "location": location,
                "subcontractor": subcontractor,
                "category": category,
                "severity": severity,
                "problem": problem,
                "suggestion": suggestion,
                "photos": uploaded_files,
                "map": map_image
            })
            st.success("✅ 已成功新增！")
            st.rerun()
        else:
            st.error("請填寫發生地點和問題事項")

with tab3:
    st.subheader("歷史報告查詢")
    if st.session_state.history:
        df = pd.DataFrame(st.session_state.history)
        st.dataframe(df)
        
        date_filter = st.date_input("過濾日期", datetime.today())
        filtered = df[df['date'] == str(date_filter)]
        if not filtered.empty:
            st.write("符合條件的報告：")
            st.dataframe(filtered)
    else:
        st.info("還沒有歷史報告")

with tab2:
    if st.button("🚀 生成 Word 報告", type="primary"):
        if not st.session_state.issues:
            st.error("請先新增問題")
        else:
            doc = Document()
            # ... (報告生成程式碼保持不變，直到 doc.save(filename) 這一行)
            
            filename = f"廣華醫院2期安全報告_{datetime.now().strftime('%Y%m%d_%H%M')}.docx"
            doc.save(filename)
            
            # 保存到歷史記錄（修正後）
            st.session_state.history.append({
                "date": str(datetime.now().date()),
                "time": datetime.now().strftime("%H:%M"),
                "issue_count": len(st.session_state.issues),
                "report_name": filename
            })
            
            with open(filename, "rb") as f:
                st.download_button("📥 下載報告", f, file_name=filename)
