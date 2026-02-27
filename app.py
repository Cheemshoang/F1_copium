from utils.data_loader import setup_cache, load_session
import streamlit as st 

st.set_page_config(
    page_title="F1 Analytics",
    page_icon="🏎️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("🏎️ F1 Analytics Dashboard")
st.markdown("Select a page from the sidebar to get started.")
