import streamlit as st
from docx import Document
from docx.shared import Inches
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO
import json
import os

st.set_page_config(page_title="廣華醫院2期地盤安全報告", layout="wide")

# 檔案路徑
DATA_FILE = "daily_issues.json"
MAP_FILE = "current_map.png"

def load_issues():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_issues(issues):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(issues, f, ensure_ascii=False, indent=2)

# 載入數據
if 'issues' not in st.session_state:
    st.session_state.issues = load_issues()
if 'map_image' not in st.session_state:
    if os.path.exists(MAP_FILE):
        with open(MAP_FILE, "rb") as f:
            st.session_state.map_image = f.read()

# Logo
st.markdown("""
<div style="text-align: center; margin-bottom: 10px;">
    <img src="https://raw.githubusercontent.com/h3699/dailysafetyreport/main/logo.png" width="280">
</div>
""", unsafe_allow_html=True)

st.title("中國水電 俊和")
st.subheader("廣華醫院2期地盤安全巡查報告系統")

company = "中國水電 俊和"
site_name = "廣華醫院2期地盤"
