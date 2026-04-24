import streamlit as st
import os

st.set_page_config(page_title="About Me", page_icon="👤")


try:
    style_path = os.path.join(os.path.dirname(__file__), "..", "style.css")
    with open(style_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
except Exception as e:
    st.error(f"Could not load styles: {e}")

st.title("👤 About Me")

st.markdown("""
    <div class="info-card">
        <p style="font-size: 1.1rem; line-height: 1.6;">
            I'm currently learning web development and building simple and user-friendly designs that make a useful projects.
        </p>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="info-card">
            <h3>🎓 Education</h3>
            <p>• Bachelor of Science in Computer Science</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="info-card">
            <h3>🚀 Goals</h3>
            <p>• Become a Web Developer</p>
            <p>• Build meaningful web designs</p>
        </div>
    """, unsafe_allow_html=True)
